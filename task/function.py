# -*- coding: UTF-8 -*-
"""功能函数"""

from datetime import datetime
import linecache
import string
import subprocess
import html
import os
import re
import shutil
import gzip
import json
import random
import sys
from io import StringIO
from urllib.parse import quote, unquote
from functools import lru_cache
import aiofiles
from zhconv import convert
# from PIL import Image
from fake_useragent import UserAgent
import tldextract
# import jiagu
# import htmlmin
# import rjsmin
# from css_html_js_minify import css_minify

import httpx
from ruamel.yaml import YAML
from src.const import CONFIG_YML, IPS_TXT, MEDIA_TYPE


class Func:
    """功能函数"""

    def __init__(self):
        self.headers = {"user-agent": UserAgent().random}
        self.yaml = YAML()
        self.yaml.default_flow_style = False
        self.yaml.indent(mapping=2, sequence=4, offset=2)
        # self.ips = self.getIPS()
        self.cache = {}
        # self.errcode = self.getYml(ERRCODE_PATH)

    async def requestGet(self,
                         url,
                         headers=None,
                         params=None,
                         follow_redirects=True,
                         use_ip="0.0.0.0"):
        """异步访问 GET"""
        headers = self.headers if headers is None else headers
        transport = httpx.AsyncHTTPTransport(local_address=use_ip)
        async with httpx.AsyncClient(http2=False,
                                     transport=transport) as client:
            resp = await client.get(
                url,
                headers=headers,
                params=params,
                follow_redirects=follow_redirects,
                timeout=15,
            )
        return resp

    async def requestPost(self,
                          url,
                          headers=None,
                          params=None,
                          datas=None,
                          use_ip="0.0.0.0"):
        """异步访问 POST"""
        transport = httpx.AsyncHTTPTransport(local_address=use_ip)
        async with httpx.AsyncClient(http2=False,
                                     transport=transport) as client:
            resp = await client.post(url,
                                     headers=headers,
                                     params=params,
                                     json=datas,
                                     timeout=15)
        return resp

    async def requestStream(self,
                            request,
                            url,
                            headers=None,
                            params=None,
                            follow_redirects=True,
                            use_ip="0.0.0.0"):
        """异步访问 GET流式"""
        headers = self.headers if headers is None else headers
        transport = httpx.AsyncHTTPTransport(local_address=use_ip)
        async with httpx.AsyncClient(http2=False,
                                     transport=transport) as client:
            try:
                async with client.stream(
                        "GET",
                        url,
                        headers=headers,
                        params=params,
                        follow_redirects=follow_redirects,
                        timeout=30,
                ) as r:
                    content_type = r.headers.get('Content-Type')
                    headers = {
                        'Content-Type': content_type,
                        "X-Cache-Mode": "Stream",
                        "Cache-Control": "public, max-age=604800"
                    }
                    response_obj = await request.respond(headers=headers)
                    async for chunk in r.aiter_bytes():
                        await response_obj.send(chunk)
                    await response_obj.eof()
            except Exception as err:
                print("异步访问 GET流式 报错：", url, str(err))

    def getIPS(self):
        """获取当前服务器所有IP"""
        nowsys = sys.platform
        if "win" in nowsys:
            return []
        try:
            ips_list = os.popen("ip addr").readlines()
            ips = []
            for i in ips_list:
                if "inet " in i:
                    i = i.strip().split(" ")[1].split("/")[0]
                    ips.append(i)
            if "127.0.0.1" in ips:
                ips.remove("127.0.0.1")
            with open(IPS_TXT, "w", encoding="utf-8") as txt_f:
                txt_f.write("\n".join(ips))
            return ips
        except Exception as err:
            print(err)
            return []

    def existsChinese(self, string):
        """判断字符串中是否存在中文"""
        for i in string:
            if "\u4e00" <= i <= "\u9fff":
                return True
        return False

    def isUrl(self, url):
        """判断url是否是网址"""
        url = url.replace('http://', '').replace('https://', '').split('/')[0]
        tld = tldextract.extract(url)
        domain = ".".join([tld.domain, tld.suffix]).lower()
        if '.' in domain and domain[-1] != "." and domain[0] != ".":
            return True
        return False

    def getDomainInfo(self, domain):
        """获取域名前后缀"""
        tld = tldextract.extract(domain)
        subdomain = tld.subdomain.lower()
        full_domain = (".".join([tld.subdomain, tld.domain,
                                 tld.suffix]).strip(".").lower())
        root_domain = ".".join([tld.domain, tld.suffix]).strip(".").lower()
        return subdomain, full_domain, root_domain

    def getText(self, path):
        """文本文件解析"""
        linecache.checkcache(path)
        text = "".join(linecache.getlines(path))
        return text

    def getLines(self, path):
        """txt文件解析"""
        linecache.checkcache(path)
        result = list(set([i.strip() for i in linecache.getlines(path)]))
        while "" in result:
            result.remove("")
        return result

    def getLine(self, path):
        return random.choice(self.getLines(path))

    # @lru_cache(maxsize=None)  # 使用 lru_cache 装饰器，maxsize=None 表示缓存大小不限制
    def getYml(self, path):
        """解析yaml文件"""
        linecache.checkcache(path)
        yml = "".join(linecache.getlines(path))
        result = self.yaml.load(yml)
        return result

    def getYmlWithStr(self, yml):
        """解析yaml str"""
        result = self.yaml.load(yml)
        return result

    # def str_to_yaml(self, yml):
    #     """str解析成yaml"""
    #     result = self.yaml.load(yml)

    async def saveYml(self, path, data):
        """保存yaml文件"""
        stream = StringIO()
        self.yaml.dump(data, stream)
        yaml_str = stream.getvalue()
        async with aiofiles.open(path, "w") as f:
            await f.write(yaml_str)

    # async def getTypeJsonInfo(self, type_path):
    #     async with aiofiles.open(type_path, "r") as json_f:
    #         json_content = await json_f.read()
    #     json_info = json.loads(json_content)
    #     return json_info

    async def getTypeJsonInfo(self, target_path):
        type_path = target_path + ".type"
        if type_path in self.cache:
            return self.cache[type_path]
        if os.path.exists(type_path):
            async with aiofiles.open(type_path, "r") as json_f:
                json_content = await json_f.read()
            if len(json_content.strip()) < 5:
                self.rm(type_path)
                # 删除目标站非200页面
                self.rm(target_path)
                json_info = {
                    "code": 404,
                    "media_type": "text/html; charset=UTF-8"
                }
            else:
                json_info = json.loads(json_content)
                self.cache[type_path] = json_info
        else:
            # 删除目标站非200页面
            self.rm(target_path)
            json_info = {"code": 404, "media_type": "text/html; charset=UTF-8"}
        return json_info

    @lru_cache(maxsize=None)
    def getStaticMediaType(self, path):
        for i in MEDIA_TYPE:
            if path.endswith(i):
                return MEDIA_TYPE[i]
        else:
            return "text/html"

    async def save_gz(self, data, path):
        """保存gzip压缩文件"""
        async with aiofiles.open(path, "wb") as gz_f:
            # 压缩数据
            data_comp = gzip.compress(data.encode())
            await gz_f.write(data_comp)

    async def show_gz(self, path):
        """解包gzip压缩文件"""
        async with aiofiles.open(path, "rb") as gz_f:
            file_content = await gz_f.read()
        result = gzip.decompress(file_content).decode()
        return result

    def del_file(self, path):
        """删除文件"""
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            print(f"已删除：{path}")
        except Exception as err:
            print(path, "删除失败", err)

    def transcoding(self, string):
        """html实体化转码"""
        new = ""
        for i in string:
            if "\u4e00" <= i <= "\u9fff":
                new += "&#" + str(ord(i)) + ";"
            else:
                new += i
        return new

    def unescape(self, string):
        """html实体解码"""
        return html.unescape(string)

    def toHant(self, string):
        """简体转繁体"""
        return convert(string, "zh-hant")

    def toZH(self, string):
        """繁体转简体"""
        return convert(string, "zh-cn")

    async def get_file_count(self, file_path):
        """快速获取文档行数"""
        return sum(1 for _ in open(file_path))

    def encryptHTML(self, html_code):
        # 加密混淆html代码
        html_code = htmlmin.minify(html_code)
        return html_code

    def encryptJS(self, js_code):
        # 加密混淆JS代码
        js_code = rjsmin.jsmin(js_code)
        return js_code

    def encryptCSS(self, css_code):
        # 加密混淆CSS代码
        css_code = css_minify(css_code)
        return css_code

    def flipImage(self, picpath):
        """翻转图片"""
        im = Image.open(picpath)
        new_pic = im.transpose(Image.FLIP_LEFT_RIGHT)
        new_pic.save(picpath)
        print(f"图片翻转成功 {picpath}")

    def getTextKeyword(self, text, k=1):
        """文本关键词抽取"""
        keywords = []
        for i in jiagu.keywords(text, 50):
            i = i.strip(". ,")
            if len(i) > 1 and not i.isdigit():
                keywords.append(i)
        if len(keywords) < k:
            k = len(keywords)
        keys = random.sample(keywords, k=k)
        return keys

    def url_get_path(self, url):
        """url文件路径解析"""
        domain = self.getDomainInfo(url)[-1]
        if url[:len("http://")] == "http://":
            url = url[len("http://"):]
        if url[:len("https://")] == "https://":
            url = url[len("https://"):]
        url = quote(url.strip("./"))
        while "./" in url:
            url = url.replace("./", "/").strip("./")
        while "//" in url:
            url = url.replace("//", "/").strip("./")
        dir_ = os.path.dirname(url)
        base_name = os.path.basename(url)
        dir_path = os.path.join(os.path.join(CACHE_PATH, domain), dir_)
        file_path = os.path.join(dir_path, base_name + ".cache")
        return file_path, dir_path

    def clean_url(self, url):
        """url路径解析"""
        sub, full_domain, domain = self.getDomainInfo(url)
        if url[:len("http://")] == "http://":
            url = url[len("http://"):]
        if url[:len("https://")] == "https://":
            url = url[len("https://"):]
        url = quote(url.strip("./"))
        while "./" in url:
            url = url.replace("./", "/").strip("./")
        while "//" in url:
            url = url.replace("//", "/").strip("./")
        url = f"http://{url}"
        return url, sub, full_domain, domain

    async def get_sql_cache(self, pool, url):
        """获取sql缓存"""
        link = self.clean_url(url)[0]
        result = None
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    sql_command = (
                        f"SELECT cache FROM spider_pool WHERE link='{link}' LIMIT 1"
                    )
                    await cur.execute(sql_command)
                    await conn.commit()
                    result = await cur.fetchone()
                    if result is not None:
                        result = result[0]
                        # 数量+1
                        sql_command = f"update spider_pool set request_count=request_count+1 WHERE link='{link}'"
                        await cur.execute(sql_command)
                        await conn.commit()
                except Exception as err:
                    print(err)
        return result

    async def save_sql_cache(self, pool, url, content, title, is_index,
                             tem_name):
        """保存sql缓存"""
        link, sub, full_domain, domain = self.clean_url(url)
        if sub == "" or sub == "www":
            url_type = "主站"
        else:
            url_type = "泛站"
        page_type = "首页" if is_index else "内页"
        data = (
            domain,
            full_domain,
            link,
            content,
            title,
            url_type,
            page_type,
            1,
            tem_name,
        )
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql_command = f"INSERT INTO spider_pool(domain,full_domain,link,cache,title,type,page_type,request_count,template) VALUE{str(data)};"
                try:
                    await cur.execute(sql_command)
                    await conn.commit()
                except Exception as err:
                    # print(err)
                    if "doesn't exist" in str(err):
                        # 开始创建字段
                        sql_command = """CREATE TABLE spider_pool(
id INT NOT NULL AUTO_INCREMENT,
domain VARCHAR(100) NOT NULL,
full_domain VARCHAR(100) NOT NULL,
link VARCHAR(500) NOT NULL,
cache LONGTEXT NOT NULL,
title VARCHAR(200),
template VARCHAR(100),
type VARCHAR(10) NOT NULL,
page_type VARCHAR(10) NOT NULL,
create_time timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
update_time timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
request_count int(100) DEFAULT NULL,
PRIMARY KEY ( id ),
UNIQUE (link)
);"""
                        await cur.execute(sql_command)
                        await conn.commit()

    async def get_cache(self, url):
        """获取本地缓存文件"""
        file_path = self.url_get_path(url)[0]
        content = None
        if os.path.exists(file_path):
            async with aiofiles.open(file_path, "r",
                                     encoding="utf-8") as cache_f:
                content = await cache_f.read()
        return content

    async def save_cache_tem(self, url, content):
        """保存缓存"""
        file_path, dir_path = self.url_get_path(url)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        async with aiofiles.open(file_path, "w", encoding="utf-8") as cache_f:
            await cache_f.write(content)

    def loading_ad_meta(self, tem, is_index, show_tem=""):
        """处理JS广告 verify验证文件"""
        if show_tem == "":
            config = self.getYml(CONFIG_YML)
            jsad = "\n".join(config["【JS广告】"]) + "\n"
            tem = tem.replace("</head>", jsad + "</head>")
        # 加verify验证文件
        if is_index:
            meta_tags = []
            for name in os.listdir(VERIFY_PATH):
                verify_file_path = os.path.join(VERIFY_PATH, name)
                linecache.checkcache(verify_file_path)
                content = "".join(linecache.getlines(verify_file_path)).strip()
                meta_tag = f'<meta name="{name}" content="{content}">'
                meta_tags.append(meta_tag)
            if len(meta_tags) > 0:
                meta = "\n".join(meta_tags)
                tem = tem.replace("</head>", meta + "\n</head>")
        return tem

    async def get_sql_tem(self, pool, link):
        """获取sql缓存"""
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    sql_command = (
                        f"SELECT template FROM spider_pool WHERE link='{link}' LIMIT 1"
                    )
                    await cur.execute(sql_command)
                    await conn.commit()
                    result = await cur.fetchone()
                    # print(result)
                    if result is not None:
                        result = result[0]
                        if result is None:
                            result = ""
                    else:
                        result = None
                except Exception as err:
                    print(err)
                    result = "error"
        return result

    async def save_sql_tem(self, pool, link, tem_name):
        """保存sql tem 缓存"""
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    # 数量+1
                    sql_command = f"update spider_pool set template='{tem_name}' WHERE link='{link}'"
                    await cur.execute(sql_command)
                    await conn.commit()
                except Exception as err:
                    print(err)

    async def get_tem_cache(self, pool, base_url, tem_name, is_index, config):
        """获取当前url的引用模板路径"""
        link, sub, full_domain, domain = self.clean_url(base_url)
        create_index_page = False
        if config["【模板策略】"]["云缓存"]:
            result = await self.get_sql_tem(pool, link)
            if result == "":
                # 存在link 但没有template 开始 update 新的模板
                await self.save_sql_tem(pool, link, tem_name)
            elif result is None:
                # 不存在首页link
                create_index_page = True
            elif result == "error":
                # 连接数据库报错 不知道存不存在link
                pass
            else:
                tem_name = result
        else:
            cache_tem_file_dir = os.path.join(CACHE_TEM_PATH, domain)
            os.makedirs(cache_tem_file_dir, exist_ok=True)
            cache_tem_file_path = os.path.join(cache_tem_file_dir,
                                               full_domain + ".yml")
            if not os.path.exists(cache_tem_file_path):
                yml_content = f"name: '{tem_name}'"
                # 写入引用模板名
                async with aiofiles.open(cache_tem_file_path,
                                         "w",
                                         encoding="utf-8") as yml_f:
                    await yml_f.write(yml_content)
            cache_tem = self.getYml(cache_tem_file_path)
            tem_name = cache_tem["name"]
        if is_index:
            tem_path = os.path.join(INDEX_DIR, tem_name)
            if not os.path.exists(tem_path):
                tem_path = os.path.join(PAGE_DIR, tem_name)
        else:
            tem_path = os.path.join(PAGE_DIR, tem_name)
        return tem_path, tem_name, create_index_page

    def parse_path(self, url_path):
        """解析url_path"""
        # url反攻击处理
        while "//" in url_path or "./" in url_path:
            url_path = url_path.replace("//", "/").replace("./", "/")
        path = url_path.strip("./").replace("/", "\\")
        path = "\\" + quote(path).replace("%5C", "\\")
        path = "" if path == "\\" else path
        return path

    def changeYML(self, yml_str, keywords):
        lines = re.findall("----------.*?\n", yml_str)
        if len(lines) > 0:
            old_line = lines[0]
            new_line = re.sub("----------.*?##########",
                              "----------【关键词】##########", lines[0])
            new_line = new_line.replace(
                "----------" + new_line.split("----------")[-1],
                "----------【关键词】")
            new_yml = yml_str.replace(old_line, new_line)
        else:
            new_yml = yml_str
        keywords_list = keywords.split(",")
        if len(keywords_list) < 2:
            new_yml = new_yml.replace("【关键词】", keywords_list[0])
        else:
            while "【关键词】" in new_yml:
                if len(keywords_list) < 1:
                    keywords_list = keywords.split(",")
                keyword = keywords_list.pop(0)
                new_yml = new_yml.replace("【关键词】", keyword, 1)
        return new_yml

    def replace_keywords_text(self, keywords_text, text):
        keywords = keywords_text.split(",")
        while "【关键词】" in text:
            if len(keywords) > 0:
                keyword = keywords.pop(0)
            else:
                keywords = keywords_text.split(",")
                keyword = keywords.pop(0)
            text = text.replace("【关键词】", keyword)
        return text

    # def getStartWebPath(self, dir_path, domain):
    #     # 使用 find 命令匹配文件名
    #     command = f"find {dir_path} -type f -name '{domain}_*'"
    #     # 调用命令并获取输出
    #     output = subprocess.check_output(command, shell=True)
    #     # 将输出转换为字符串并按行分割
    #     file_names = output.decode("utf-8").split("\n")
    #     # 打印匹配的文件名
    #     # for file_name in file_names:
    #     #     print(file_name)
    #     print('getStartWebPath: ', file_names)
    #     return file_names[0]

    def getStartWebPath(self, dir_path, domain):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.startswith(f"{domain}_"):
                    file_name = os.path.join(root, file)
                    # print('getStartWebPath: ', file_name)
                    return file_name
        return ""  # 如果没有找到匹配的文件，返回None或者适当的默认值

    def getFileNameStartWith(self, dir_path, start_str):
        """获取以*开头的所有文件名"""
        # 使用 find 命令匹配文件名
        command = f"find {dir_path} -type f -name '{start_str}*'"
        # 调用命令并获取输出
        output = subprocess.check_output(command, shell=True)
        # 将输出转换为字符串并按行分割
        file_names = output.decode("utf-8").split("\n")
        # 打印匹配的文件名
        # for file_name in file_names:
        #     print(file_name)
        return file_names

    def transPath(self, path):
        """编译路径"""
        path = path.rstrip('/')
        return path.replace("/", "\\")

    def realPath(self, path):
        """解析路径"""
        return path.replace("\\", "/")

    def rm(self, path):
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        except Exception as err:
            print(f"删除报错：{err} from {path}")

    async def baiduPullWord(self, word, second_mode=False):
        """百度下拉词"""
        try:
            url = f"https://suggestion.baidu.com/su?wd={word}"
            use_ip = random.choice(self.ips)
            transport = httpx.AsyncHTTPTransport(local_address=use_ip)
            async with httpx.AsyncClient(transport=transport) as client:
                resp = await client.get(
                    url,
                    headers={"user-agent": UserAgent().random},
                    timeout=15)
            pull_down_words = []
            result_list = eval(resp.text.split(',s:')[1][:-3])
            for i in result_list:
                pull_down_words.append(i)
            if pull_down_words == [] and second_mode:
                keyword = self.getTextKeyword(word, k=1)
                print('百度拆', word, keyword)
                pull_down_words = await self.baiduPullWord(keyword,
                                                           second_mode=True)
            return pull_down_words
        except Exception as err:
            print(err)
            return []

    async def googlePullWords(self, word, second_mode=False):
        """谷歌下拉词"""
        try:
            url = f"https://www.google.com/complete/search?q={word}&client=gws-wiz-serp&xssi=t&hl=zh-CN&authuser=0"
            use_ip = random.choice(self.ips)
            transport = httpx.AsyncHTTPTransport(local_address=use_ip)
            async with httpx.AsyncClient(transport=transport) as client:
                resp = await client.get(
                    url,
                    headers={"user-agent": UserAgent().random},
                    timeout=15)
            pull_down_words = []
            result_list = eval(resp.text.split('\n')[1])[0]
            for i in result_list:
                pull_down_words.append(i[0])
            if pull_down_words == [] and second_mode:
                keyword = self.getTextKeyword(word, k=1)
                print('谷歌拆', word, keyword)
                pull_down_words = await self.googlePullWords(keyword,
                                                             second_mode=True)
            return pull_down_words
        except Exception as err:
            print(err)
            return []

    def pastTime(self, file_path):
        # 获取文件创建时间
        timestamp = os.path.getctime(file_path)
        file_time = datetime.fromtimestamp(timestamp)
        # 获取当前时间
        current_time = datetime.now()
        # 计算相差的天数
        difference = current_time - file_time
        days_difference = difference.days
        # print(f"{file_path} 创建于{days_difference}天前")
        return days_difference

    def randomString(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
