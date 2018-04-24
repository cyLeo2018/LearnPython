class Fruit():
    price = 0

    def __init__(self):
        self.__color = 'red'

    def getColor(self):   #公有方法
        print(self.__color)

    @ staticmethod #@ classmethod  静态方法/类方法
    def getPrice():
        print(Fruit.price)

    def __getPrice():
        Fruit.price += 10
        print(Fruit.price)

    count = staticmethod(__getPrice) #把__getPrice()转换为静态方法，并赋值给count，也即count()为静态方法

if __name__ == '__main__':
    apple = Fruit()
    apple.getColor()
    Fruit.count()
    banana = Fruit()
    Fruit.count()
    Fruit.getPrice()
