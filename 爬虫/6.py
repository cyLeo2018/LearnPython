from urllib import request, parse
import json

baseurl = "http://fanyi.baidu.com/sug"
kw = input("Pleae input a keyword:")
data = {
    "kw":kw
}
data = parse.urlencode(data).encode("utf-8")
print(type(data))

headers = {
    "Content-Length":len(data)
}

req = request.Request(baseurl, data=data, headers=headers)
rsp = request.urlopen(req)

json_data = rsp.read().decode("utf-8")
print(type(json_data))
print(json_data)
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)
for item in json_data['data']:
    print(item)
