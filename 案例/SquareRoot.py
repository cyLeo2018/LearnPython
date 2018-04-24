# -*- encoding:UTF-8 -*-
import cmath

Num = float(input("请输入一个数字："))

if Num >= 0:
    NumSqrt = Num ** 0.5
    print("%0.3f 的平方根为:%0.3f" % (Num,NumSqrt))
else:
    NumSqrt = cmath.sqrt(Num)
    print("{0}的平方根为:{1:0.3f} + {2:0.3f}j".format(Num,NumSqrt.real,NumSqrt.imag))

