class Fruit():
    price = 0 #类属性

    def __init__(self):
        self.color = 'red' #实例属性
        zone = 'China' #局部变量,不能被实例化对象调用
        __number = 100 #私有属性

class Apple(Fruit):
    pass

if __name__ == '__main__':
    print(Fruit.price) #返回类属性
    apple = Fruit()
    print(apple.color) #返回实例属性
    #报错 print(apple.zone)
    Fruit.price += 10
    print(apple.price)
    banana = Fruit()
    print(banana.price)
    #报错 print(banana._Fruit__number)
    print(Fruit.__dict__) #Fruit类的内置属性__dict__
    print(Fruit.__bases__) #Fruit类的内置属性__bases__
    print(Fruit.__module__) #Fruit类的内置属性__module__
    print(Fruit.__doc__) #Fruit类的内置属性__doc__
