# Определяем функцию create_spreadsheet
def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " с " + str(row_count) + " строками.")

# Вызываем функцию с заголовком "Загрузки"
create_spreadsheet("Загрузки")

# Вызываем функцию с заголовком "Приложения" и количеством строк 10
create_spreadsheet("Приложения", 10)
