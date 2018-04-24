from urllib import request, error

if __name__ == "__main__":
    url = "http://www.baidu.com"
    try:
        proxy = {"http":"61.136.163.183:8104"}
        proxy_handler = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_handler)
        request.install_opener(opener)

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HTTPError:{0}".format(e.reason))
        print("HTTPError:{0}".format(e))
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)