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

# Создаем переменную  и устанавливаем ее равной 0
total_exercises = 0

# Проходим по значениям в словаре num_exercises и добавляем каждое значение в total_exercises
for exercises in num_exercises.values():
    total_exercises += exercises

print(total_exercises)
