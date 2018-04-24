#format格式化输出字符串
print('我是{0},我今年{1}岁'.format('Leo',28))
print('我是{name},我今年{age}岁'.format(name='Leo',age=28))
print('我是{0[0]},我今年{0[1]}岁'.format(('Leo',28)))
print('我是{0[n]},我今年{0[a]}岁'.format({'n':'Leo','a':28}))

print('π的值大约为：{0}'.format(3.1415926535897932384626433832795))
print('π的值大约为：{0:.2f}'.format(3.1415926535897932384626433832795))

print('10的二进制：{0:b}'.format(10))
print('10的八进制：{0:o}'.format(10))
print('10的十进制：{0:d}'.format(10))
print('10的十六进制：{0:x}'.format(10))

print('我的存款有：{0:,}元'.format(100000000))

print('{0:*<8}'.format('1'))
print('{0:->8}'.format('1'))
print('{0:|^8}'.format('1'))

#打印*组成的矩形
m_long = int(input('Please input long:'))
m_wide = int(input('Please input wide:'))
for row in range(m_long):
    for list in range(m_wide):
            print('*',end=' ')
    print()

#打印*组成的矩形，只有边框
m_long = int(input('Please input long:'))
m_wide = int(input('Please input wide:'))
for row in range(m_long):
    for list in range(m_wide):
        if (row == 0 or row == m_long-1) or (list == 0 or list == m_wide-1):
            print('*',end=' ')
        #else:
            print(' ',end=' ')
    print()

#打印直角三角形
m_long = int(input('Please input long:'))
m_wide = int(input('Please input wide:'))
for row in range(m_long):
    for list in range(row+1):
        print('*',end=' ')
    print()

#打印九九乘法口诀表
m_long = int(input('Please input long:'))
m_wide = int(input('Please input wide:'))
for row in range(1,m_long):
    for list in range(1,row+1):
        print('{0}X{1}={2}'.format(row,list,row*list),end=' ')
    print()

