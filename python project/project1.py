data = list(range(1, 21))
genap = list(filter(lambda x: x % 2 == 0, data))
kuadrat = list(map(lambda y: y * y, genap))
print(kuadrat)