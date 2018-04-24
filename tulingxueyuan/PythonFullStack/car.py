'''
表示汽车的类
'''

class Car():
    '''
    模拟汽车
    '''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #为属性'汽车里程数'指定默认值0

    def get_descriptive_name(self):
        '''
        返回汽车信息摘要
        :return:
        '''
        return '{0} {1} {2}'.format(self.year,self.make,self.model).title()

    def update_odometer(self, mileage):
        '''
        更新里程数
        禁止将里程数回调
        '''
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        '''
        汽车里程数增加指定的值
        禁止将里程数回调，也即禁止增加负数值
        :param miles:
        :return:
        '''
        if miles > 0:
            self.odometer_reading += miles
        else:
            print('You can\'t roll back an odometer!')

    def read_odometer(self):
        '''
        返回汽车里程数
        '''
        print('This car has {0} miles on it'.format(self.odometer_reading))


class ElectricCar(Car): #子类ElectricCar继承父类Car
    '''
    电动汽车
    '''
    def __init__(self, make, model, year):
        '''
        初始化父类属性
        初始化电动汽车特有属性
        :param make:
        :param model:
        :param year:
        '''
        super().__init__(make, model, year) #调用父类的方法__init__(),让ElectricCar实例包含Car类的所有属性
        self.battery = Battery() #新增属性，此时会生成新的实例Battery,将新的实例作为属性赋值给self.battery,也就是说，每当创建ElectricCar实例，初始化时，会同步创建新的Battery实例


    def fill_gas_tank(self): #重写父类的方法fill_gas_tank
        '''
        电动汽车没有邮箱
        :return:
        '''
        print('This car doesn\'t need a gas tank!')

class Battery():
    '''
    模拟电动汽车的电瓶
    '''
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a {0} -kwh battery.'.format(self.battery_size))

    def get_range(self):
        '''
        返回续航里程
        :return:
        '''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print('This car go approximately {0} miles on a full charge.'.format(range))
