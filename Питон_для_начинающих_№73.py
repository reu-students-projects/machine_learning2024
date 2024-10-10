import csv  
import datetime  
import json  

# Создание файла csv с названием 'employees.csv' для записи
with open('employees.csv', 'w', newline='') as csvfile:
    # Определение имен колонок в CSV файле
    fieldnames = ['ФИО', 'Должность', 'Дата найма', 'Оклад', 'Пол']
    # Создание объекта для записи данных в формате CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Запись заголовков 
    # Запись данных о сотруднике
    writer.writerow({'ФИО': 'Иванов Иван', 'Должность': 'Менеджер', 'Дата найма': '22.10.2013', 'Оклад': 250000, 'Пол': 'Мужской'})
    writer.writerow({'ФИО': 'Сорокина Екатерина Матвеевна', 'Должность': 'Аналитик', 'Дата найма': '12.03.2020', 'Оклад': 75000, 'Пол': 'Женский'})
    writer.writerow({'ФИО': 'Струков Иван Сергеевич', 'Должность': 'Старший программист', 'Дата найма': '23.04.2012', 'Оклад': 150000, 'Пол': 'Мужской'})
    writer.writerow({'ФИО': 'Корнеева Анна Игоревна', 'Должность': 'Ведущий программист', 'Дата найма': '22.02.2015', 'Оклад': 120000, 'Пол': 'Женский'})
    writer.writerow({'ФИО': 'Старчиков Сергей Анатольевич', 'Должность': 'Младший программист', 'Дата найма': '12.11.2021', 'Оклад': 50000, 'Пол': 'Мужской'})
    writer.writerow({'ФИО': 'Бутенко Артем Андреевич', 'Должность': 'Архитектор', 'Дата найма': '12.02.2010', 'Оклад': 200000, 'Пол': 'Мужской'})
    writer.writerow({'ФИО': 'Савченко Алина Сергеевна', 'Должность': 'Старший аналитик', 'Дата найма': '13.04.2016', 'Оклад': 100000, 'Пол': 'Женский'})

# Функция для расчета премии программистам
def calculate_programmer_bonus(employees):
    bonuses = []  # Список для хранения премий программистов
    for employee in employees:  # Итерация по списку сотрудников
        if 'программист' in employee['Должность'].lower():  # Проверка, есть ли слово "программист" в должности
            bonus = float(employee['Оклад']) * 0.03  # Вычисление премии 
            bonuses.append({'ФИО': employee['ФИО'], 'Премия': bonus})  #Добавление информации о премии в список
    return bonuses  

# Функция для расчета праздничной премии
def calculate_holiday_bonus(employees, date):
    bonuses = []  # Список для хранения праздничных премий
    for employee in employees:  # Итерация по списку сотрудников
        if date == datetime.date(date.year, 3, 8) and employee['Пол'].lower() == 'женский':
            bonuses.append({'ФИО': employee['ФИО'], 'Премия': 2000})  #Добавление информации о премии
        elif date == datetime.date(date.year, 2, 23) and employee['Пол'].lower() == 'мужской':
            bonuses.append({'ФИО': employee['ФИО'], 'Премия': 2000})  #Добавление информации о премии
    return bonuses  

# Функция для расчета индексации зарплаты
def calculate_salary_indexation(employees):
    indexed_employees = []  # Список для хранения индексаций зарплат
    for employee in employees:  # Итерация по списку сотрудников
        hire_date = datetime.datetime.strptime(employee['Дата найма'], '%d.%m.%Y').date()  # Преобразование даты найма в объект даты
        current_date = datetime.date.today()  # Получение текущей даты
        years_worked = (current_date - hire_date).days / 365  # Расчет количества лет работы
        # Проверка, если сотрудник работает более 10 лет
        if years_worked >= 10:
            indexation = int(employee['Оклад']) * 0.07  # Индексация 7%
        else:
            indexation = int(employee['Оклад']) * 0.05  # Индексация 5%
        indexed_employees.append({'ФИО': employee['ФИО'], 'Индексация': indexation})  # Добавление информации о индексации в список
    return indexed_employees  

# Функция для составления графика отпусков
def get_vacation_schedule(employees):
    vacation_employees = []  # Список для сотрудников, имеющих право на отпуск
    for employee in employees:  # Итерация по списку сотрудников
        hire_date = datetime.datetime.strptime(employee['Дата найма'], '%d.%m.%Y').date()  # Преобразование даты найма в объект даты
        current_date = datetime.date.today()  # Получение текущей даты
        months_worked = ((current_date - hire_date).days / 30)  # Расчет отработанных месяцев
        # Проверка, если сотрудник работает более 6 месяцев
        if months_worked >= 6:
            vacation_employees.append({'ФИО': employee['ФИО']})  # Добавление информации о праве на отпуск в список
    return vacation_employees  

# Функция для записи данных в csv
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:  # Открытие файла для записи
        fieldnames = data[0].keys()  # Получение имен колонок из первого элемента данных
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # Создание объекта для записи в формате CSV
        writer.writeheader()  # Запись заголовков колонок
        writer.writerows(data)  # Запись всех строк данных в файл

# Функция для записи данных в json
def save_to_json(data, filename):
    with open(filename, 'w') as jsonfile:  # Открытие файла для записи
        json.dump(data, jsonfile, indent=4)  # Запись данных в формате JSON с отступами

# Чтение данных из файла csv
with open('employees.csv', 'r') as csvfile:  # Открытие файла для чтения
    reader = csv.DictReader(csvfile)  # Создание объекта для чтения данных в формате CSV
    employees = list(reader)  # Преобразование данных в список словарей

# Вычисление премий программистам
programmer_bonuses = calculate_programmer_bonus(employees)
# Вычисление праздничных премий к 8 марта
march_bonuses = calculate_holiday_bonus(employees, datetime.date(2024, 3, 8))
# Вычисление праздничных премий к 23 февраля
february_bonuses = calculate_holiday_bonus(employees, datetime.date(2024, 2, 23))

# Вычисление индексации зарплаты
indexed_salaries = calculate_salary_indexation(employees)

# Составление графика отпусков
vacation_schedule = get_vacation_schedule(employees)

# Сохранение результатов в CSV файлы
save_to_csv(programmer_bonuses, 'programmer_bonuses.csv')  # Сохранение данных о премиях программистов
save_to_csv(march_bonuses, 'march_bonuses.csv')  # Сохранение данных о премиях к 8 марта
save_to_csv(february_bonuses, 'february_bonuses.csv')  # Сохранение данных о премиях к 23 февраля
save_to_csv(indexed_salaries, 'indexed_salaries.csv')  # Сохранение данных о индексации зарплат
save_to_csv(vacation_schedule, 'vacation_schedule.csv')  # Сохранение данных о графике отпусков

# Сохранение результатов в JSON файлы
save_to_json(programmer_bonuses, 'programmer_bonuses.json')  # Сохранение данных о премиях программистов в JSON формате
save_to_json(march_bonuses, 'march_bonuses.json')  # Сохранение данных о премиях к 8 марта в JSON формате
save_to_json(february_bonuses, 'february_bonuses.json')  # Сохранение данных о премиях к 23 февраля в JSON формате
save_to_json(indexed_salaries, 'indexed_salaries.json')  # Сохранение данных об индексации зарплат в JSON формате
save_to_json(vacation_schedule, 'vacation_schedule.json')  # Сохранение данных о графике отпусков в JSON формате

