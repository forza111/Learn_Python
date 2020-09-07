class Personal():
    def __init__(self):
        print('добро пожаловать на наш сайт')
    def login(self, login, password):
        self.login = login
        self.password = password
        if login == 'Forza'and password == 'n94i3k6':
            print(self.login + ' Вы вошли в систему')
        else:
            print('Вы ввели неправильные данные')

ogyzok = Personal()

