# Вводим имя пользователя
user_name = input("Введите ваше имя: ")

# Вводим номер АРМ (
ARM = int(input("Введите номер АРМ: "))

# Устанавливаем соответствие имен пользователей и номеров АРМ
users_ARMs = {
    "Дмитрий": 1,
    "Ангелина": 2,
    "Василий": 3,
    "Екатерина": 4
}

# Проверяем соответствие имени и номера АРМ
if user_name in users_ARMs:
    if users_ARMs[user_name] == ARM:
        print("Добро пожаловать!")
    elif user_name == "Дмитрий":
        print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
    else:
        print("Логин или пароль не верный, попробуйте еще раз")
else:
    print("Пользователь не найден.")
