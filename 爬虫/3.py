from urllib import request,parse

if __name__ == "__main__":
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")
    qs = {
        "wd":wd
    }
    qs = parse.urlencode(qs) #编码
    print(qs)
    fullurl = url + qs
    print(fullurl)
