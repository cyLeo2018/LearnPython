# -*- encoding:UTF-8 -*-
import cmath

a,b,c = input("输入三个数字(空格分隔):").split()

print("二元方程:{0}x**2+{1}x+{2} = 0".format(a,b,c))

d = float(b)**2 - 4*float(a)*float(c)
Result1 = (-float(b)-cmath.sqrt(float(d)))/(2*float(a))
Result2 = (-float(b)+cmath.sqrt(float(d)))/(2*float(a))

if d >= 0:
    print("Result:{0},{1}".format(Result1,Result2))
else :
    print("No result!")