class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def description_name(self):
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()
    def read_odometer(self):
        '''Выводим пробег авто'''
        print('Пробег этого авто ' + str(self.odometer_reading) + ' km')
    def update_odometer(self, km):
        '''Устанавливаем значение на одометре'''
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Не стоит баловаться уважаемый!')
    def increment_odometer(self,km):
        '''Увеличиваем показания одометра на заданную величину
        upd: Увеличиваем только на положительное число'''
        if km >= 0:
            self.odometer_reading += km
        else:
            print('Откручивать пробег нельзя, уважаемый')
opel = Car('Opel', 'Astra', 2008)
#opel.odometer_reading = 900
opel.update_odometer(90)
opel.increment_odometer(100)


#opel.read_odometer()

'''Наследование'''

class  Battery():
    '''Простая модель аккумулятора для автомобиля'''
    def __init__(self,battery = 100):
        self.battery = battery
    def description_battery(self):
        '''Выводит информацию о мощности батареи'''
        print('Этот автомобиль имеет батарею мощностью ' + str(self.battery) + ' кВ')


class Electriccar(Car):
    def __init__(self,make,model,year):
        '''Инициализация атрибутов класса родителя'''
        super().__init__(make, model, year)
        #self.battery = 100
        self.battery = Battery()

    def description_battery(self):
        '''Выводит информацию о мощности батареи'''
        print('Этот автомобиль имеет батарею мощностью ' + str(self.battery) + ' кВ')
    def description_name(self):
        '''Переопределение родительского метода'''
        desc = str(self.year) + ' ' + self.model
        return desc.title()

tesla = Electriccar('tesla', 'model S', 2019)

#print(opel.description_name())
#tesla.description_battery()
#print(tesla.description_name())
tesla.battery.description_battery()
'''Обращаемся к экземпляру класа Тесла и артибуту battery,который в свою очередь
является классом Battery 'description_battery' - метод в классе Battery'''

