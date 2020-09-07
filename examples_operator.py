def bigger_price(limit,data):
    '''Данная функция создана для вывода самых дорогих товаров. Функция принимает два
    аргумента: limit - число (сколько товаров из списка необходимо вывести),например 2
               data - список словарей вида:
        [{'name': 'wine', 'price' : 12},
         {'name': 'coca- cola', 'price' : 10},
           {'name': 'Mac-book', 'price': 120}
        ]
        данная функция вернет:[{'name': 'Mac-book', 'price': 120},
        {'name': 'wine', 'price': 12}]
        '''
    from operator import itemgetter
    max_price = sorted(data, key = itemgetter('price'),reverse=True)
    return(max_price[0:limit])


