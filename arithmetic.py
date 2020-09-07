def arithmetic(a,b,operator):
    '''Описание: данная функция имеет 2 числа и оператор. В зависимости от введенного
    оператора будут происходить разные действия с числами'''
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a*b
    if operator == '/':
        return a/b
    else:
        print('Данной функции не сущетвует')
print (arithmetic((int(input('Введите первое число'))),(int(input('Введите второе число'))),input('Введите операцию')))