def split_join():
#Описание: данная программа  принимает на ввод строку - на выходе заменяет пробелы
#на нижние подчеркивания, при этом удаляет лишние пробелы, если их было несколько,
#и вместо n-го количества пробелов заменяет на один знак '_'
    a = input('')
    print('_'.join(a.split()))
split_join()
