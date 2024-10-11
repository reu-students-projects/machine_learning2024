# Определяем функцию repeat_stuff
def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats  # Возвращаем повторяющуюся строку

# Вызов функции с аргументами "Row" и 3
lyrics = repeat_stuff("Row", 3) + " Your Boat."  # Объединяем результат с "Your Boat."

# Создаем переменную song, вызывая функцию только с stuff
song = repeat_stuff("Row")  # Используется значение по умолчанию для num_repeats

print(song)
