class Fruit():
    def __init__(self, color):
        self.color = color
        print('Fruit\'s color:{0}'.format(self.color))

    def grow(self):
        print('Grow...')

class Apple(Fruit):
    def __init__(self, color):
        Fruit.__init__(self, color)
        print('apple\'s color:{0}'.format(self.color))

class Banana(Fruit):
    def __init__(self, color):
        Fruit.__init__(self, color)
        print('banana\'s color:{0}'.format(self.color))

    def grow(self):
        print('banana grow...')

apple1 = Apple('red')
apple1.grow()
banana1 =Banana('yellow')
banana1.grow()
