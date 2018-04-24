# list1 = [1,2,3,4,5]
# list2 = [11,22,33,44,55]
# z = zip(list1, list2)
# print(type(z))
# print(z)
# for i in z:
#     print(i)

list1 = ["zhangsan","lisi","wangwu"]
list2 = [99,67,100]
z = zip(list1,list2)
print(type(z))
print(z)
# for i in z:
#     print(i)
list3 = [i for i in z]
print(type(list3))
print(list3)