import car

my_beetle = car.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())
my_beetle.odometer_reading = 23
my_beetle.read_odometer()

my_tesla = car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
