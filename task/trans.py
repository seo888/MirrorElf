# -*- coding: UTF-8 -*-
"""翻译"""

import time
import random
import re
import hashlib
from urllib.parse import unquote, quote
from fake_useragent import UserAgent
import httpx
from lxml import etree


class AsyncYouDao:
    """有道网页翻译"""

    async def get_resp(self, url, use_ip):
        """获取有道源码"""
        headers = {
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1049708127.9005697",
            "Host": "webtrans.yodao.com",
            "Referer": "http://webtrans.yodao.com/webTransPc/index.html",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UserAgent().random,
        }

        headers = self.headers if headers is None else headers
        transport = httpx.AsyncHTTPTransport(local_address=use_ip)
        async with httpx.AsyncClient(http2=False,
                                     transport=transport) as client:
            return await client.get(
                url,
                headers=headers,
                follow_redirects=True,
                timeout=30,
            )

    async def webTrans(self,
                       target_url,
                       from_lang="auto",
                       to_lang="auto",
                       use_ip='0.0.0.0'):
        "网页翻译"
        if from_lang == "zh":
            from_lang = "zh-CHS"
        if to_lang == "zh":
            to_lang = "zh-CHS"
        o = str(int(time.time() * 1000) + random.randint(1, 10))
        r = "ydsecret://mdictweb.si/sign/-eV=8}L$s4$nPL00op3p]"
        real_target_url = target_url
        if "&" in target_url:
            if "/" in (t_u_split := target_url.split("?", 1))[-1]:
                start_, end_ = t_u_split
                target_url = start_ + "?" + end_.replace('/', '%2F')
                real_target_url = target_url
            t = quote(target_url, safe="")
        else:
            t = target_url
        s = "mdictweb"
        c = s + o + r + real_target_url
        md5 = hashlib.md5()
        md5.update(c.encode("utf8"))
        c_md5 = md5.hexdigest()
        url = "http://webtrans.yodao.com/server/webtrans/tranUrl?url={}&from={}&to={}&type=1&product=mdictweb&salt={}&sign={}".format(
            t, from_lang, to_lang, o, c_md5)
        retry_count = 0
        while True:
            resp = await self.get_resp(url, use_ip)
            source = resp.text.replace("&amp;", "&")
            if "很抱歉，您输入的网址不存在或当前无法访问，请稍后重试" in source:
                if retry_count > 1:
                    return {"success": False, "source": source}
                retry_count += 1
                print(f"翻译失败: 重试第{retry_count}次 {target_url}")
            elif resp.status_code != 200:
                print(f"翻译失败: {target_url} 状态码：{resp.status_code}")
                return {"success": False, "source": source}
            else:
                titles = re.findall("<title.*?>(.*?)</title>", source,
                                    re.IGNORECASE)
                title = "" if len(titles) == 0 else titles[0]
                if any(i in title
                       for i in ["404", "异常访问", "no found", "not found"]):
                    print(f"翻译失败: {target_url} 404 no found")
                    return {"success": False, "source": source}
                elif any(i in source for i in [
                        "<title>404</title>",
                        "页面已被删除",
                        "页面未找到",
                        "输入的地址不正确",
                        "403 Forbidden",
                ]):
                    return {"success": False, "source": source}
                print(f"翻译代理: {target_url}")
                break
        tree = etree.HTML(source)
        for i in tree.xpath("//a/@href"):
            if len(i.strip()) > 1:
                try:
                    url = i
                    s = re.search("url=(.*?)&from", url)
                    b = unquote(unquote(s.group(1)))
                    source = source.replace(i, b)
                except Exception as err:
                    print(i, err)
        source = re.sub('<base href=".*?">', "", source)
        trans_from = re.search("TransFrom: '(.*?)'", source).group(1)
        trans_to = re.search("TransTo: '(.*?)'", source).group(1)
        source = re.sub(r"<script>var getParameter[\s\S]*</script>", "",
                        source)
        return {
            "success": True,
            "from": trans_from,
            "to": trans_to,
            "source": source
        }


class YouDao:
    """有道网页翻译"""

    def webTransResp(self, url, use_ip):
        """获取有道源码"""
        headers = {
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1049708127.9005697",
            "Host": "webtrans.yodao.com",
            "Referer": "http://webtrans.yodao.com/webTransPc/index.html",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UserAgent().random,
        }

        headers = self.headers if headers is None else headers
        transport = httpx.HTTPTransport(local_address=use_ip)
        with httpx.Client(http2=True, transport=transport) as client:
            return client.get(
                url,
                headers=headers,
                follow_redirects=True,
                timeout=30,
            )

    def webTrans(self,
                 target_url,
                 from_lang="auto",
                 to_lang="auto",
                 use_ip='0.0.0.0'):
        "网页翻译"
        if from_lang == "zh":
            from_lang = "zh-CHS"
        if to_lang == "zh":
            to_lang = "zh-CHS"
        o = str(int(time.time() * 1000) + random.randint(1, 10))
        r = "ydsecret://mdictweb.si/sign/-eV=8}L$s4$nPL00op3p]"
        real_target_url = target_url
        if "&" in target_url:
            if "/" in (t_u_split := target_url.split("?", 1))[-1]:
                start_, end_ = t_u_split
                target_url = start_ + "?" + end_.replace('/', '%2F')
                real_target_url = target_url
            t = quote(target_url, safe="")
        else:
            t = target_url
        s = "mdictweb"
        c = s + o + r + real_target_url
        md5 = hashlib.md5()
        md5.update(c.encode("utf8"))
        c_md5 = md5.hexdigest()
        url = "http://webtrans.yodao.com/server/webtrans/tranUrl?url={}&from={}&to={}&type=1&product=mdictweb&salt={}&sign={}".format(
            t, from_lang, to_lang, o, c_md5)
        retry_count = 0
        while True:
            resp = self.webTransResp(url, use_ip)
            source = resp.text.replace("&amp;", "&")
            if "很抱歉，您输入的网址不存在或当前无法访问，请稍后重试" in source:
                if retry_count > 1:
                    return {
                        "success": False,
                        "source": "很抱歉，您输入的网址不存在或当前无法访问，请稍后重试"
                    }
                retry_count += 1
                print(f"翻译失败: 重试第{retry_count}次 {target_url}")
            elif resp.status_code != 200:
                print(f"翻译失败: {target_url} 状态码：{resp.status_code}")
                return {
                    "success": False,
                    "source": f"翻译失败: {target_url} 状态码：{resp.status_code}"
                }
            else:
                titles = re.findall("<title.*?>(.*?)</title>", source,
                                    re.IGNORECASE)
                title = "" if len(titles) == 0 else titles[0]
                if any(i in title
                       for i in ["404", "异常访问", "no found", "not found"]):
                    print(f"翻译失败: {target_url} 404 no found")
                    return {
                        "success": False,
                        "source": f"翻译失败: {target_url} 404 no found"
                    }
                elif any(i in source for i in [
                        "<title>404</title>",
                        "页面已被删除",
                        "页面未找到",
                        "输入的地址不正确",
                        "403 Forbidden",
                ]):
                    return {"success": False, "source": "<title>404</title>"}
                print(f"翻译代理: {target_url}")
                break
        tree = etree.HTML(source)
        for i in tree.xpath("//a/@href"):
            if len(i.strip()) > 1:
                try:
                    url = i
                    s = re.search("url=(.*?)&from", url)
                    b = unquote(unquote(s.group(1)))
                    source = source.replace(i, b)
                except Exception as err:
                    print(i, err)
        source = re.sub('<base href=".*?">', "", source)
        trans_from = re.search("TransFrom: '(.*?)'", source).group(1)
        trans_to = re.search("TransTo: '(.*?)'", source).group(1)
        source = re.sub(r"<script>var getParameter[\s\S]*</script>", "",
                        source)
        return {
            "success": True,
            "from": trans_from,
            "to": trans_to,
            "source": source
        }

    def trans(self,
              need_trans_list,
              from_lang="AUTO",
              to_lang="AUTO",
              use_ip='0.0.0.0'):
        headers = {
            'Cookie':
            'OUTFOX_SEARCH_USER_ID=-690213934@10.108.162.139; OUTFOX_SEARCH_USER_ID_NCOO=1273672853.5782404; fanyi-ad-id=308216; fanyi-ad-closed=1; ___rl__test__cookies=1659506664755',
            'Host': 'fanyi.youdao.com',
            'Origin': 'https://fanyi.youdao.com',
            'Referer': 'https://fanyi.youdao.com/',
            "User-Agent": UserAgent().random,
        }
        # key = need_trans_list
        key = "\n".join(need_trans_list)
        lts = str(int(time.time() * 100))
        salt = lts + str(random.randint(0, 9))
        sign_data = 'fanyideskweb' + key + salt + 'Ygy_4c=r#e#4EX^NUGUc5'
        sign = hashlib.md5(sign_data.encode()).hexdigest()
        data = {
            'i': key,
            'from': from_lang,
            'to': to_lang,
            # 'smartresult': 'list',
            'client': 'fanyideskweb',
            # 时间戳  1970  秒
            'salt': salt,
            # 加密
            'sign': sign,
            # 时间戳
            'lts': lts,
            # 加密的数据
            'bv': 'f0819a82107e6150005e75ef5fddcc3b',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        # 获取到资源地址
        url = 'https://fanyi.youdao.com/translate_o'
        transport = httpx.HTTPTransport(local_address=use_ip)
        with httpx.Client(http2=True, transport=transport) as client:
            result = client.post(url, data=data, headers=headers,
                                 timeout=30).json()
        print(result)
        if result['errorCode'] == 0:
            result_dict = {}
            for i in result['translateResult']:
                for ii in i:
                    result_dict[ii['src']] = ii['tgt']
            return result_dict
        return {}


if __name__ == "__main__":
    url = 'https://www.socalgas.com'
    result = YouDao().webTrans(url, to_lang='zh')
    print(result)
    with open('index.html', encoding='utf-8') as f:
        f.write(result['source'])
