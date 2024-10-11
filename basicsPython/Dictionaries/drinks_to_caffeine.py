# Списки напитков и их содержание кофеина
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Создаем итеративный тип с парами напитков и кофеина
zipped_drinks = zip(drinks, caffeine)

# Генерируем словарь из итератора zipped_drinks
drinks_to_caffeine = {drink: mg_caffeine for drink, mg_caffeine in zipped_drinks}

print(drinks_to_caffeine)
