import requests

url = "http://www.baidu.com"
rsp = requests.get(url)
print(type(rsp))
print(rsp.text)

rsp = requests.request("get", url)

