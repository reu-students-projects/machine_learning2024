# Генерируем список с помощью range
list1 = range(2, 20, 2)

# Вычисляем длину list1
list1_len = len(list1)

# Проверяем длину list1
print("Длина list1:", list1_len)

# Изменяем команду range, чтобы пропускать 3 вместо 2
list1 = range(2, 20, 3)

# Проверяем новую длину list1
new_list1_len = len(list1)
print("Новая длина list1:", new_list1_len)
