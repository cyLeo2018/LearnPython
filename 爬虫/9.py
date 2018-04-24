from urllib import request, error

if __name__ == "__main__":
    url = "http://www.baidu.com"
    try:
        # headers = {}
        # headers["User-Agent"]="Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
        # req = request.Request(url, headers=headers)
        # rsp = request.urlopen(req)
        # # print(rsp.info())
        # html = rsp.read().decode()
        # # print(html)

        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")
        rsp = request.urlopen(req)
        print(rsp.info())
        html = rsp.read().decode()
        # print(html)
    except error.HTTPError as e:
        print("HTTPError:{0}".format(e.reason))
        print("HTTPError:{0}".format(e))
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)