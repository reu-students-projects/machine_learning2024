# Создаём список вещей в чемодане
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']

# Проверяем переменную beginning
beginning = suitcase[0:2]
print("Первые два элемента:", beginning)
print("Количество элементов в beginning:", len(beginning))

# Изменяем beginning, чтобы оно выделяло первые 4 элемента
beginning = suitcase[0:4]
print("Первые четыре элемента:", beginning)

# Создаём новый список middle, содержащий два средних элемента
middle = suitcase[2:4]
print("Средние элементы:", middle)
