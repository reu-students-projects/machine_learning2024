# Словарь с идентификаторами пользователей
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# Словарь с количеством упражнений по разным темам
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# Получаем объект  для всех ключей словаря user_ids
users = user_ids.keys()

# Получаем объект  для всех ключей словаря num_exercises
classes = num_exercises.keys()

print(users)

print(classes)
