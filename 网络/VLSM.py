from IPy import IP

ip_s = input("Please input an IP or net-range:")
ips = IP(ip_s)
if len(ips) > 1:
    print("Net:%s" % ips.net())
    print("NetMask:%s" % ips.netmask())
    print("Broadcast:%s" % ips.broadcast())
    print("Reverse Address:%s" % ips.reverseNames()[0])
    print("Subnet:%s" % len(ips))
else:
    print("Reverse Address:%s" % ips.reverseNames()[0])

print("Hexadecimal:%s" % ips.strHex())
print("Binary IP:%s" % ips.strBin())
print("IPtype:%s" % ips.iptype())
