import os
import functools
import random

# print(os.getcwd())
# os.chdir('E:\Learn\python\\Notebook\Theory')
# print(os.getcwd())
# print(os.listdir())
# print(os.getenv('path').replace(';','\n'))
# print(os.curdir) #当前目录
# print(os.pardir) #父目录
# print(os.sep) #路径分隔符
# print(os.linesep) #系统换行符号
# print(os.name) #系统名
# print(os.path.abspath('.'))

# a1 = [i*10 for i in range(1,11)]
# b1 = list(map(lambda x:x*10,range(1,11)))
# c1 = list(map(lambda x,y:x+y,range(1,11),range(1,11)))
# print(type(functools.reduce(lambda x,y:x+y,range(1,101))))

print(random.random()) #随机生成0-1之间的浮点数
print(random.uniform(1,10)) #随机生成1-10之间的浮点数
print(random.randint(1,100)) #随机生成1-100之间的整数
print(random.randrange(1,101,2)) #随机生成在1-100之间以步长2递增的数字集合中的整数
print(random.choice(range(101))) #随机从指定序列中获取元素

a1 = [1,2,3,4,5,6]
print(random.sample(a1,2)) #随机从指定序列中获取指定长度的元素并随机排列


