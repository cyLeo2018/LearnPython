list1 = ['a','b','c','d','e']
em = enumerate(list1)
list2 = [i for i in em]
# print(type(list2))
# print(list2)

em2 = enumerate(list1, start=100)
list3 = [i for i in em2]
print(type(list3))
print(list3)

