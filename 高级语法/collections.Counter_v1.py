from collections import Counter

c = Counter('ashsydfgjkasdaklsdasd')
print(type(c))
print(c)
for k,v in c.items():
    print(k,':','出现',v,'次')


# s = ['leo','cy','cy','zhangsan','zhangsan']
# c = Counter(s)
# print(type(c))
# print(c)
# for k,v in c.items():
#     print(k,':','出现',v,'次')
