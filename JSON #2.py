import json
filename = 'user.json'
try:
    with open(filename) as f:
        user = json.load(f)
except:
    username = input('Введите ваше имя')
    with open(filename,'w', encoding='utf-8') as fl:
       json.dump(username,fl, ensure_ascii=False)
       print('Мы запомним вас, как ' + username)
else:
    print('добро пожаловать ' + user + '!')