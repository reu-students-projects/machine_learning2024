# Добавляем "matcha" в словарь с уровнем кофеина
caffeine_level = {
    "espresso": 64,
    "chai": 40,
    "decaf": 0,
    "drip": 120,
    "matcha": 30  
}

# Пытаемся вывести уровень кофеина для matcha
try:
    print(f"Уровень кофеина в матче: {caffeine_level['matcha']} мг")
except KeyError:
    print("Неизвестный уровень кофеина")
