# Определяем функцию calc_age
def calc_age(current_year, birth_year):
    age = current_year - birth_year  # Вычисляем возраст
    return age  # Возвращаем возраст

# Вызываем функцию с текущим годом 2049 и годом рождения 1993
my_age = calc_age(2049, 1993)

# Вызываем функцию с текущим годом 2049 и годом рождения 1953
dads_age = calc_age(2049, 1953)

print(f"Мне {my_age} лет, а моему отцу {dads_age} лет.")
