from urllib import request, error

if __name__ == "__main__":
    url = "http://study.163.com/my"
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")
        # print(html)
        with open("163study.html", "w", encoding="utf-8") as f: #注意编码utf-8
            f.write(html)

    except error.HTTPError as e:
        print("HTTPError:{0}".format(e.reason))
        print("HTTPError:{0}".format(e))
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)