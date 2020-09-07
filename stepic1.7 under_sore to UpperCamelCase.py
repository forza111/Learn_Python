def under_score():
    '''Описание: данная программа принимает на вооде строку, записанную в формате
    underscore?? и выводит строку в формате UpperCamelCase.
     Например:
     ввод: my_first_class
     вывод: MyFirstClass'''
    import re
    b = input('')
    a = re.split(r'_',b.title())
    print(''.join(a))
under_score()