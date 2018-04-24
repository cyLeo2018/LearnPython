from urllib import request

if __name__ == "__main__":
    url = "http://www.baidu.com/"
    rsp = request.urlopen(url)  #打开URL获取页面,返回的是对象
    print(rsp.geturl()) #获取URL地址
    print(rsp.info()) #获取HTTP报文头信息
    print(rsp.getcode()) #获取HTTP状态码
    html = rsp.read() #读取返回结果，数据为字节流ASCII Bytes
    print(type(html)) #字节流bytes
    html = html.decode() #将字节流bytes解码为字符串
    print(html) #打印页面
