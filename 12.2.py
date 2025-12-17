print("prices = 1500, 500, 2000, 3500, 1000, 4500")
prices = [1500, 500, 2000, 3500, 1000, 4500]

print(f"Самый дорогой товар{max(prices)}")
print(f"Самый дешевый товар{min(prices)}")
print(f"Общая сумма товаров{sum(prices)}")
print(f"Средная цена товара{int(sum(prices)/len(prices))}")