import chardet
from urllib import request

if __name__ == "__main__":
    url = "http://www.baidu.com"
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html) #检测页面编码,返回字典；chardet.detect()检测对象是字节流
    print(type(cs)) #返回字典
    print(cs)
    html = html.decode(cs.get("encoding", "utf-8")) #根据字典键"encoding"获取编码格式，如果没有，则设置为utf-8

