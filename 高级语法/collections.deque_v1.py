from collections import deque

q = deque(['a','b','c'])
print(type(q))
print(q)
q.append('d')
print(q)
q.appendleft('x')
print(q)
