def best_stock(stocks):
    from collections import defaultdict

    mirror = defaultdict(list)
    for a, v in stocks.items():
        mirror[v].append(a)

    answer = max(mirror.keys())
    return (mirror.get(answer))

print(best_stock({'gazprom': 10, 'neftegaz': 102, 'sber': 12,'tatneft':102}))