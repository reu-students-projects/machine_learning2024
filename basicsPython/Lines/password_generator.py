# Функция для генерации временного пароля
def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]

first_name = "Виталий"
last_name = "Красилов"
temp_password = password_generator(first_name, last_name)

print("Временный пароль:", temp_password)
