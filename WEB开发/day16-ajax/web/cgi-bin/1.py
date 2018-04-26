import cgi,cgitb,json,time


cgitb.enable()
print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()
inputs = {}
for key in fs.keys():
    inputs[key] = fs[key].value
print(inputs)
# print(json.dumps(inputs))