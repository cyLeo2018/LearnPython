from urllib import request, parse
import json

baseurl = "http://fanyi.baidu.com/sug"
kw = input("Pleae input a keyword:")
data = {
    "kw":kw
}
data = parse.urlencode(data).encode("utf-8") #使用utf-8将str编码为Bytes流
print(type(data))
# headers = {
#     "Content-Length":len(data)
# }
rsp = request.urlopen(baseurl, data=data) #urlopen data格式为字节流
json_data = rsp.read().decode("utf-8") #使用utf-8将Bytes流解码为str
print(type(json_data))
print(json_data)
json_data = json.loads(json_data) #使用json将str转换成json格式，返回字典
print(type(json_data))
print(json_data)
for item in json_data['data']:
    print(item)
