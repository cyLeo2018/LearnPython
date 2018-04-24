import collections

# Point = collections.namedtuple("Point",['x','y'])
# p = Point(11,22)
# print(p.x)
# print(p[1])

Circle = collections.namedtuple("Circle",['x','y','r'])
c = Circle(100,150,50)
print(type(c))
print(c)
print(isinstance(c,tuple))
