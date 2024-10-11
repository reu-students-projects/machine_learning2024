# Функция для генерации имени учетной записи
def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

first_name = "Виталий"
last_name = "Красилов"
new_account = account_generator(first_name, last_name)

print("Новая учетная запись:", new_account)
