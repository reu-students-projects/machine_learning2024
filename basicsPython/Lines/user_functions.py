# Функция для генерации имени пользователя
def username_generator(first_name, last_name):
    # Получаем первые три буквы имени
    username_first_part = first_name[:3] if len(first_name) >= 3 else first_name
    # Получаем первые четыре буквы фамилии
    username_second_part = last_name[:4] if len(last_name) >= 4 else last_name
    # Объединяем и возвращаем имя пользователя
    return username_first_part + username_second_part

# Функция для генерации временного пароля
def password_generator(username):
    password = ""  # Инициализируем пустую строку для пароля
    # Проверяем, пустое ли имя пользователя
    if username:
        # Перебираем символы в имени пользователя
        for i in range(len(username)):
            # Сдвигаем все буквы на одну вправо
            # Если это последний символ, добавляем его перед всеми остальными
            if i == len(username) - 1:
                password = username[i] + password  # Добавляем последний символ в начало
            else:
                password += username[i]  # Добавляем текущий символ в конец
    return password

first_name = "Abe"
last_name = "Simpson"
username = username_generator(first_name, last_name)
temp_password = password_generator(username)

print(f"Сгенерированное имя пользователя: {username}")
print(f"Сгенерированный временный пароль: {temp_password}")
