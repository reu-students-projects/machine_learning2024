import csv

# Изначальные данные сотрудников
data = [
    {"name": "Иванов Иван Иванович", "position": "Менеджер", "hire_date": "22.10.2013", "salary": 250000},
    {"name": "Сорокина Екатерина Матвеевна", "position": "Аналитик", "hire_date": "12.03.2020", "salary": 75000},
    {"name": "Струков Иван Сергеевич", "position": "Старший программист", "hire_date": "23.04.2012", "salary": 150000},
    {"name": "Корнеева Анна Игоревна", "position": "Ведущий программист", "hire_date": "22.02.2015", "salary": 120000},
    {"name": "Старчиков Сергей Анатольевич", "position": "Младший программист", "hire_date": "12.11.2021",
     "salary": 50000},
    {"name": "Бутенко Артем Андреевич", "position": "Архитектор", "hire_date": "12.02.2010", "salary": 200000},
    {"name": "Савченко Алина Сергеевна", "position": "Старший аналитик", "hire_date": "13.04.2016", "salary": 100000}
]
# Открываем (создаём) файл CSV для записи
with open('employees.csv', 'w', newline='', encoding='utf-8') as output_csv:
    # Определяем заголовки столбцов
    fields = ['name', 'position', 'hire_date', 'salary']

    # Создаём объект writer, который будет записывать словари в CSV файл
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)

    # Записываем заголовок (первую строку)
    output_writer.writeheader()

    # Записываем данные сотрудников
    for employee in data:
        output_writer.writerow(employee)

print("Файл employees.csv успешно создан!")
print()




#1. создание функции премии
def calculate_bonus(salary):
    return salary * 0.03  # возвращаем 3% от оклада

#список сотрудников с их должностями и окладами
employees = [
    {"name": "Иванов Иван Иванович", "position": "Менеджер", "salary": 250000},
    {"name": "Струков Иван Сергеевич", "position": "Старший программист", "salary": 150000},
    {"name": "Корнеева Анна Игоревна", "position": "Ведущий программист", "salary": 120000},
    {"name": "Старчиков Сергей Анатольевич", "position": "Младший программист", "salary": 50000},
    {"name": "Сорокина Екатерина Матвеевна", "position": "Аналитик", "salary": 75000},
    {"name": "Бутенко Артем Андреевич", "position": "Архитектор", "salary": 200000}
]
# фильтруем список, оставляя только программистов
programmers = [employee for employee in employees if "программист" in employee["position"]]
# вычисляем и выводим премии для программистов
for programmer in programmers:
    bonus = calculate_bonus(programmer["salary"])  # рассчитываем премию
    print(programmer["name"] + ": " + str(round(bonus, 2)) + " рублей")

print()





# 2. Премии к 8 марта и 23 февраля
def calculate_holiday_bonus(employee):
    # возвращаем 2000 рублей в зависимости от пола сотрудника
    if employee['gender'] == 'female':
        return 2000  # премия для женщин
    elif employee['gender'] == 'male':
        return 2000  # премия для мужчин
    else:
        return 0  # если пол не определен, премии нет
# Список сотрудников с их полом, должностями и окладами
employees = [
    {"name": "Иванов Иван Иванович", "gender": "male", "position": "Менеджер", "salary": 250000},
    {"name": "Сорокина Екатерина Матвеевна", "gender": "female", "position": "Аналитик", "salary": 75000},
    {"name": "Струков Иван Сергеевич", "gender": "male", "position": "Старший программист", "salary": 150000},
    {"name": "Корнеева Анна Игоревна", "gender": "female", "position": "Ведущий программист", "salary": 120000},
    {"name": "Старчиков Сергей Анатольевич", "gender": "male", "position": "Младший программист", "salary": 50000},
    {"name": "Бутенко Артем Андреевич", "gender": "male", "position": "Архитектор", "salary": 200000}
]
# вывод премий для сотрудников
for employee in employees:
    bonus = calculate_holiday_bonus(employee)  # рассчитываем премию
    total_salary = employee["salary"] + bonus  # рассчитываем итоговый оклад
    print(employee["name"] + ": Премия - " + str(bonus) + " рублей, Итоговый оклад - " + str(
        total_salary) + " рублей")

print()

#индексация зп
from datetime import datetime

def calculate_salary_increase(employee):
    # определяем текущую дату
    current_date = datetime.now()
    hire_date = datetime.strptime(employee['hire_date'], "%d.%m.%Y")  # преобразуем строку в дату
    years_worked = (current_date - hire_date).days // 365  # рассчитываем количество лет работы

    # определяем процент индексации в зависимости от стажа
    if years_worked > 10:
        return employee["salary"] * 0.07  # 7% для сотрудников с стажем более 10 лет
    else:
        return employee["salary"] * 0.05  # 5% для остальных

# список сотрудников с их полом, должностями, окладами и датами найма
employees = [
    {"name": "Иванов Иван Иванович", "gender": "male", "position": "Менеджер", "salary": 250000, "hire_date": "22.10.2013"},
    {"name": "Сорокина Екатерина Матвеевна", "gender": "female", "position": "Аналитик", "salary": 75000, "hire_date": "12.03.2020"},
    {"name": "Струков Иван Сергеевич", "gender": "male", "position": "Старший программист", "salary": 150000, "hire_date": "23.04.2012"},
    {"name": "Корнеева Анна Игоревна", "gender": "female", "position": "Ведущий программист", "salary": 120000, "hire_date": "22.02.2015"},
    {"name": "Старчиков Сергей Анатольевич", "gender": "male", "position": "Младший программист", "salary": 50000, "hire_date": "12.11.2021"},
    {"name": "Бутенко Артем Андреевич", "gender": "male", "position": "Архитектор", "salary": 200000, "hire_date": "12.02.2010"}
]

# вывод зарплат с учетом индексации
for employee in employees:
    bonus = calculate_holiday_bonus(employee)  # рассчитываем премию
    salary_increase = calculate_salary_increase(employee)  # рассчитываем индексацию
    total_salary = employee["salary"] + bonus + salary_increase  # рассчитываем итоговый оклад
    print(employee["name"] +  " Индексация - " + str(round(salary_increase, 2)) + " рублей, Итоговый оклад - " + str(round(total_salary, 2)) + " рублей")

print()

# 4.отпуска более 6 мес работы
# функция для фильтрации сотрудников, отработавших более 6 месяцев
def filter_long_term_employees(employees):
    current_date = datetime.now()
    long_term_employees = []

    for employee in employees:
        hire_date = datetime.strptime(employee['hire_date'], "%d.%m.%Y")
        months_worked = (current_date - hire_date).days // 30  # количество отработанных месяцев

        if months_worked > 6:  # если отработано больше 6 месяцев
            long_term_employees.append(employee)

    return long_term_employees


# получаем список сотрудников, отработавших более 6 месяцев
long_term_employees = filter_long_term_employees(data)

# выводим список
print("Сотрудники, отработавшие более 6 месяцев:")
for employee in long_term_employees:
    print(employee['name'] + ",  Дата найма: " + employee['hire_date'] )
print()





import json

# Данные сотрудников
employees = [
    {
        'name': "Иванов Иван Иванович",
        'position': "Менеджер",
        'hire_date': "22.10.2013",
        'salary': 250000,
        'gender': 'male'
    },
    {
        'name': "Сорокина Екатерина Матвеевна",
        'position': "Аналитик",
        'hire_date': "12.03.2020",
        'salary': 75000,
        'gender': 'female'
    },
    {
        'name': "Струков Иван Сергеевич",
        'position': "Старший программист",
        'hire_date': "23.04.2012",
        'salary': 150000,
        'gender': 'male'
    },
    {
        'name': "Корнеева Анна Игоревна",
        'position': "Ведущий программист",
        'hire_date': "22.02.2015",
        'salary': 120000,
        'gender': 'female'
    },
    {
        'name': "Старчиков Сергей Анатольевич",
        'position': "Младший программист",
        'hire_date': "12.11.2021",
        'salary': 50000,
        'gender': 'male'
    },
    {
        'name': "Бутенко Артем Андреевич",
        'position': "Архитектор",
        'hire_date': "12.02.2010",
        'salary': 200000,
        'gender': 'male'
    },
    {
        'name': "Савченко Алина Сергеевна",
        'position': "Старший аналитик",
        'hire_date': "13.04.2016",
        'salary': 100000,
        'gender': 'female'
    }
]

with open('employees.json', 'w', encoding='utf-8') as json_file:
    json.dump(employees, json_file, ensure_ascii=False, indent=4)

print("Данные сотрудников успешно записаны в employees.json")


