from urllib import request, parse, error

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1523801875178",
        "sign": "e5f91dd9d8d1b3a96940e0ef1fe50ef2",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    data = parse.urlencode(data).encode("utf-8")
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN, zh;q=0.9, en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": 204,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a |;OUTFOX_SEARCH_USER_ID=739938809@61.140.184.233;JSESSIONID=abcBCgIkR-HmqcjvRQjlw;OUTFOX_SEARCH_USER_ID_NCOO=1587448692.969935;_ntes_nnid=28144eead274172d513b5d0980c9e85c, 1523801858595;___rl__test__cookies=1523801875176",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

if __name__=="__main__":
    youdao("girl")
