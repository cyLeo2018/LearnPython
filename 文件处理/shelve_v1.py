import shelve

# shv = shelve.open(r'shv.db')
# print(type(shv))
# print(shv)
# shv['one'] = 1
# shv['two'] = 2
# shv['three'] = 3
# print(shv)
# shv.close()

shv = shelve.open(r'shv.db')
print(shv['one'])
print(shv['three'])
shv.close()