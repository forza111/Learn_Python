'''Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел,
объединённых бинарным оператором: a operator b, где вместо operator

могут использоваться следующие слова: plus, minus, multiply, divide для,
соответственно, сложения, вычитания, умножения и целочисленного деления.
пайтон своифункции
Формат ввода:
Одна строка, содержащая выражение вида a operator b
, 0≤a,b≤1000

. Оператор может быть plus, minus, multiply, divide.

Формат вывода:
Строка, содержащая целое число −
результат вычисления.'''

def calculator(a, operator, b):
    if a>0 and b<1000:
     if operator == 'plus':
        return round(a+b)
     if operator == 'minus':
        return round(a-b)
     if operator == 'multiply':
        return round(a*b)
     if operator == 'divide':
        return a//b
    else:
         print('Ошибка')
print(calculator())
