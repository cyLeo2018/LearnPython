def make_pizza(price, size='10寸', *args, **kwargs): # 初始*toppings是空元组，存放传递过来的实参
    '''
    返回披萨所有配料
    :param toppings:
    :return:
    '''
    for i in args:
        print('- {0}'.format(i))

make_pizza('$10','15寸','mushrooms', 'green peppers', 'extra cheese')