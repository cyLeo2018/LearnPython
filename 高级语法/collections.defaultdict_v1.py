# dict1 = {'a':1,'b':2,'c':3}
# print(dict1['d'])

from collections import defaultdict

d2 = defaultdict(lambda :"Hello")
d2['a'] = 1
d2['b'] = 2
print(d2['b'])
print(d2['c'])

