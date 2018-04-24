from urllib.parse import urlparse

o1 = urlparse("http://www.cwi.nl:80/%7Eguido/Python.html")
o2 = urlparse("//www.cwi.nl:80/%7Eguido/Python.html")
o3 = urlparse("www.cwi.nl/%7Eguido/Python.html")
o4 = urlparse("help/Python.html")
o5 = urlparse("wj8w.com")

print(type(o1))
print("URL:{0}  {1}".format(o1.geturl(), o1))
print(o1.scheme)
print(o1.netloc)
print(o1.path)
print(o1.geturl())

print("URL:{0}  {1}".format(o2.geturl(), o2)) #netloc的识别从//开始
print("URL:{0}  {1}".format(o3.geturl(), o3)) #如果没有识别到netloc，则认为是path
print("URL:{0}  {1}".format(o4.geturl(), o4))
print("URL:{0}  {1}".format(o5.geturl(), o5))


