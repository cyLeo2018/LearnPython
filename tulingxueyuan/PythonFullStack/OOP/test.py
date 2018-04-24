def func(n):
    for i in range(n):
        yield i

r = func(10)
print(r)