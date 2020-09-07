def bigger_price(limit,data):
    from operator import itemgetter
    max_price = sorted(data, key = itemgetter('price'),reverse=True)

    return(max_price[0:limit])

print(bigger_price(2,[{'name':'kakawka', 'price':30},{'name':'zalypa','price':10},
     {'name':'sychara','price':20
      }]))