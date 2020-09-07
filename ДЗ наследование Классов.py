class Restraunt():
    def __init__(self, name, food, drink, starry_restraunt):
        self.name = name
        self.food = food
        self.drink = drink
        self.starry_restraunt = starry_restraunt
    def seats(self):
        self.seat = 100
        print('Ресторан ' + self.name + ' имеет ' + str(self.seat)+' посадочных мест')
    def working_hours(self):
        self.work = 24
        print('Ресторан ' + self.name + ' работает ' + str(self.work) + ' часов')
    def number_of_matching(self):
        self.number = 100
        print('В ресторане ' + self.name + ' работает' + str(self.number) + ' соотрудников')
class Hookah(Restraunt):
    '''Создаем дочерний класс кальян от класса ресторан'''
    def __init__(self, name, food, drink, starry_restraunt):
        super().__init__(name, food, drink, starry_restraunt)
        self.sort = 'Virginia'
    def order_a_hookah(self):
        print('Прошу принести кальян с табаком ' + self.sort)

eleon = Hookah('Bygaga','LOL','ALALAL', 6)

eleon.order_a_hookah()
eleon.seats()
print(eleon.sort)
