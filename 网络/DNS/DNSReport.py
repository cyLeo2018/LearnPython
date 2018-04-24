import dns.resolver
import os
import httplib

iplist = []
appdomain = "www.google.com.hk"

def get_iplist(domain = ""):
    A = dns.resolver.query(domain,"A")
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET","/",headers = {"Host":appdomain})
        r = conn.getresponse()
        getcontent = r.read(15)
        print(getcontent)
    #finally:
    #    if getcontent == r"<!doctype html>"
    #        print(ip,"[OK]")
    #    else:
    #        print(ip,"[Error]")


if get_iplist(appdomain) and len(iplist) > 0 :
    for ip in iplist:
        checkip(ip)
else:
    print("DNS resolver error!")
