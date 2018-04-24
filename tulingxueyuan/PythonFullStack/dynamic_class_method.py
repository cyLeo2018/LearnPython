class Fruit():
    pass

def add(self):
    print('Grow...')

Fruit.grow = add #将新定义的方法add，直接动态加入到Fruit类中，重命名为grow
fruit1 = Fruit()
fruit1.grow() #调用新增加的grow方法
