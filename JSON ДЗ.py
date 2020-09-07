import json





filename = 'love.json'
try:
    with open(filename) as f:
        lovenums1 = json.load(f)
except:
    lovenums = input('Введите ваше любимое число')
    with open(filename, 'a',encoding='utf-8') as fl:
        json.dump(lovenums, fl,ensure_ascii=False)
        print('Я знаю ваше любимое число, этooooo ' + lovenums)
else:
    print('Я знаю ваше любимое число, это ' + lovenums1)
