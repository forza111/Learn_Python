def matematica(a,b,c=''):
    if c:
        if c == '+':
            return ( a + b)
        if c == '-':
            return ( a - b)
        if c == '*':
            return ( a * b)
        if c == '/':
            return ( a / b)
        else:
            print('Некоректный знак')
    else:
        return (a + b)
