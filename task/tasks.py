import base64
import traceback
from celery import Celery
import httpx
from fake_useragent import UserAgent
import redis
import chardet
import re
from urllib.parse import urlparse, urljoin
from lxml import html as lxml_html
import html
from yarl import URL
from trans import YouDao

IPS_TXT = "config/IPS.txt"
REDIS_DEBUG_ADDR = "redis://localhost"
RABBITMQ_DEBUG_ADDR = 'amqp://admin:mirrorelf@localhost//'

# 初始化 Celery
celery_app = Celery('tasks',
                    broker=RABBITMQ_DEBUG_ADDR,
                    backend='rpc://',
                    result_expires=300)
celery_app.conf.update({
    'broker_connection_retry_on_startup': True,
    'worker_prefetch_multiplier': 1,
    'task_acks_late': True,
    'task_reject_on_worker_lost': True,
    'worker_concurrency': 512,
})

redis_client = redis.from_url(REDIS_DEBUG_ADDR, max_connections=100)
youdao = YouDao()
# translator = LocalTrans()
ua = UserAgent(platforms='pc')
redirect_paths = {
    "", "/index.html", "/index.php", "/index.asp", "/index.jsp", "/index.htm",
    "/index.shtml", "/index", "/home.html"
}


def autodetect(content):
    """自动检测内容编码"""
    return chardet.detect(content).get("encoding")


def make_relative(url, base_url, attribute):
    """将绝对 URL 转换为相对 URL"""
    parsed_url = urlparse(url)
    if not base_url.startswith(('http://', 'https://')):
        base_url = f'{parsed_url.scheme}://{base_url}'
    parsed_base = urlparse(base_url)

    if parsed_url.netloc == parsed_base.netloc:
        relative_path = urljoin('', parsed_url.path)
        if parsed_url.query:
            relative_path += f'?{parsed_url.query}'
        if parsed_url.fragment:
            relative_path += f'#{parsed_url.fragment}'
        return relative_path
    elif attribute == 'src':
        return f"/-/{url.replace('http://','').replace('https://','')}"
    return url


def replace_absolute_with_relative(text, base_url):
    """在 HTML 文本中替换绝对 URL 为相对 URL"""

    def replace(match):
        attribute = match.group(1)
        url = match.group(2)
        return f'{attribute}="{make_relative(url, base_url, attribute)}"'

    pattern = r'(href|src)=["\'](https?://[^"\']+)["\']'
    new_text = re.sub(pattern, replace, text)
    return new_text


def prepare_translation(url, lang, to_lang, use_ip):
    """执行翻译"""
    trans_result = youdao.webTrans(str(url),
                                   from_lang=lang,
                                   to_lang=to_lang,
                                   use_ip=use_ip)
    if not trans_result["success"]:
        raise ValueError(f'Translator Error {trans_result["source"]}')
    return trans_result["source"]


def parse_html(url, content, lang, to_lang, use_ip):
    """解析 HTML 内容，替换 URL 并检查页面是否需要翻译"""
    base_url = url.host
    translated_dict = {}
    if lang == to_lang:
        source = replace_absolute_with_relative(content, base_url)
        tree = lxml_html.fromstring(source) if source else None
    else:
        source = prepare_translation(url, lang, to_lang, use_ip)
        source = replace_absolute_with_relative(source, base_url)
        tree = lxml_html.fromstring(source)
        # 翻译title description alt title属性
        # 收集待翻译的文本
        texts_to_translate = []
        title_element = tree.find(".//title")
        title = ''
        if title_element is not None and len(title_element.text) > 1:
            title = title_element.text
            texts_to_translate.append(title)
        description_element = tree.find(".//meta[@name='description']")
        description = ''
        if description_element is not None and 'content' in description_element.attrib and len(
                description_element.attrib['content']) > 1:
            description = description_element.attrib['content']
            texts_to_translate.append(description)

        else:
            description_element = tree.find(
                ".//meta[@property='og:description']")
            if description_element is not None and 'content' in description_element.attrib and len(
                    description_element.attrib['content']) > 1:
                description = description_element.attrib['content']
                texts_to_translate.append(description)
        # 一次性翻译所有收集到的文本
        translated_dict = youdao.trans(texts_to_translate,
                                       from_lang=lang.upper(),
                                       to_lang=to_lang.upper(),
                                       use_ip=use_ip)
        # 删除所有 img 标签的 alt 和 title 属性
        remove_alt_title_attributes(tree)
    # 找到所有以 "twitter:" 开头的 meta 标签并删除它们
    for meta in tree.xpath('//meta[starts-with(@name, "twitter:")]'):
        meta.getparent().remove(meta)
    # 找到 <html> 标签并修改 lang 属性
    html_element = tree.xpath('//html')[0] if tree.xpath('//html') else None
    if html_element is not None:
        html_element.set('lang', to_lang)
    return tree, translated_dict


def remove_alt_title_attributes(tree):
    """删除所有标签的 alt 和 title 属性"""
    for element in tree.iter():
        if 'alt' in element.attrib:
            del element.attrib['alt']
        if 'title' in element.attrib:
            del element.attrib['title']


def extract_title_and_status(tree):
    """提取页面标题和状态码"""
    title = tree.findtext('.//title') if tree is not None else ''
    title = title.strip() if title else ''
    status_code = 404 if len(title) < 2 or any(
        keyword in title for keyword in ['404错误', '404 Error']) else 200
    return title, status_code


def predownload_links(tree, url, deep):
    """执行页面预下载"""
    elements = tree.xpath(
        "//a[not(starts-with(@href, 'http')) and not(starts-with(@href, '//'))]"
    )
    deep_save_set = set()
    for element in elements:
        link = element.get('href', '')
        if not link:
            element.set('href', "/")
            continue
        if ":" in link:
            continue
        if not link.startswith('/'):
            new_path = f"{url.path.rsplit('/',1)[0]}/{link}"
            element.set('href', new_path)
            new_url = f"{url.host}{new_path}"
        else:
            new_url = f"{url.host}{link}"
        if deep < 1:
            deep_save_set.add(new_url.split('#')[0])
    return deep_save_set


def save_to_database(url_str, to_lang, status_code, content_type, title,
                     content):
    data = {
        "url": url_str,
        "lang": to_lang,
        "status_code": status_code,
        "content_type": content_type,
        "title": title,
        "content": content
    }
    """将数据保存到数据库"""
    with httpx.Client(limits=httpx.Limits(
            max_connections=1000, max_keepalive_connections=200)) as client:
        res = client.post('http://127.0.0.1:16888/_api_/target_cache/insert',
                          json=data,
                          timeout=10)
    return res.text


def get_response(url, referer, use_ip):
    referer = str(url.with_path('')) if referer is None else referer
    transport = httpx.HTTPTransport(local_address=use_ip,
                                    limits=httpx.Limits(
                                        max_connections=1000,
                                        max_keepalive_connections=200))
    with httpx.Client(default_encoding=autodetect,
                      transport=transport) as client:
        response = client.get(str(url),
                              headers={
                                  "Referer": referer,
                                  "User-Agent": ua.random
                              },
                              follow_redirects=True,
                              timeout=10)
    return response


@celery_app.task
def save_target_source(target_url, lang, to_lang, deep=0, referer=None):
    """Celery 任务：下载目标站资源并保存到数据库"""
    try:
        url = URL(f"http://{target_url}")
        use_ip = redis_client.srandmember(IPS_TXT).decode('utf-8')
        response = get_response(url, referer, use_ip)

        url_str = target_url
        status_code = response.status_code
        content_type = response.headers.get('Content-Type',
                                            '').strip().lower().replace(
                                                'gbk2312', 'gb2312')
        title = ''
        content = ''

        if response.status_code == 200:
            # 使用 yarl 解析原始 URL 和跳转后的 URL
            original_path = URL(url).path.strip("/")
            final_path = URL(str(response.url)).path.strip("/")
            if original_path not in redirect_paths and final_path in redirect_paths:
                status_code = 404
            elif 'text/html' in content_type:
                # html页面
                tree, translated_dict = parse_html(
                    url, html.unescape(response.text), lang, to_lang, use_ip)
                title, status_code = extract_title_and_status(tree)
                deep_save_set = predownload_links(tree, url, deep)
                for new_url in deep_save_set:
                    task_id = f"{new_url} | 语言:{lang} 译为:{to_lang}"  # 防止任务重复
                    save_target_source.apply_async(
                        (new_url, lang, to_lang, deep + 1),
                        task_id=task_id,  # 指定唯一的任务 ID
                        priority=deep + 1,
                        kwargs={'referer': str(url)})
                source = lxml_html.tostring(tree,
                                            pretty_print=True,
                                            encoding='unicode')
                source = html.unescape(source)
                # 处理翻译结果
                for k, i in translated_dict.items():
                    source = source.replace(k, i)
                # 解码
                content = base64.b64encode(
                    source.encode('utf-8')).decode('utf-8')

                url_str = f'{target_url}[{to_lang}]'
                content_type = 'text/html'
            else:
                # 静态资源
                content = base64.b64encode(response.content).decode('utf-8')

        result = save_to_database(url_str, to_lang, status_code, content_type,
                                  title, content)
        print(f'成功下载并保存：{target_url}')
        return f"[{use_ip}|{deep} {lang}]{target_url} {result}"

    except Exception as e:
        error_message = f"Error {lang}|{target_url}: {str(e)}"
        error_traceback = traceback.format_exc()
        print(f"Error occurred: {error_message}\n{error_traceback}")
        return f"{error_message}\n{error_traceback}"
