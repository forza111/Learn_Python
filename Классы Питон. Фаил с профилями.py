class User():
    def __init__(self, first_name, last_name, age, gender):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.gender = gender
    def describe_user(self):
        print('Информация о пользователе:\n' + 'Имя: ' + self.firstname + '\nФамиллия:' + self.lastname + '\nВозраст: ' + self.age + '\nПол: ' + self.gender)
    def greet_user(self):
        print('Приветствуем вас, Mr(Mrs)' + self.firstname + self.lastname)
Forza = User('Никита', ' Ионкин', '25', 'M')
Nataly = User('Наталья', ' Куприянова', '23', 'W')
McLaren = User('Некитон',' Ллллларин', '27', 'M')

Nataly.greet_user()
Nataly.describe_user()

Forza.greet_user()
Forza.describe_user()
