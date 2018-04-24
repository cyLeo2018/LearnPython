# -*- encoding:UTF-8 -*-

a,b,c = input("输入三角形三个边长(空格间隔):").split()

s = (int(a) + int(b) + int(c))/2
Area = (s*(s-int(a))*(s-int(b))*(s-int(c)))**0.5
print("Area:%.2f" % Area)
