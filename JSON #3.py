import json

def get_username():
    '''Получаем имя пользователя, если оно есть'''
    filename = 'user1.json'
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user
def get_new_username():
    '''Получаем имя пользователя, если вы не являетесь последним пользователем'''
    username = input('Введите ваше имя')
    filename = 'user1.json'
    with open(filename, 'w', encoding='utf-8') as f2:
        json.dump(username, f2, ensure_ascii=False)
        print('Мы тебя запомним, как ' + username)

def greet_user():
    '''Приветствие пользователя'''
    username = get_username()
    if username:
        a = input('Последним пользователем, использовавшим данное устройство был\n' + username +', это ваши инициалы? Поставьте "Y" если да и "N" если нет ')
        if a == 'Y':
            print('Добро пожаловать ' + username + '!')
        if a == 'N':
            username = get_new_username()
    else:
        username = input('Введите ваше имя')
        filename = 'user1.json'
        with open (filename,'w',encoding='utf-8') as fl:
            json.dump(username,fl, ensure_ascii=False)
            print('Мы тебя запомним, как ' + username)
greet_user()
