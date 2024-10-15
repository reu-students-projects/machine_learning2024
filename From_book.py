import csv
import json
from datetime import datetime

# Данные о сотрудниках
employees = [
    ["ФИО", "Должность", "Дата найма", "Оклад"],
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]

# Запись в файл CSV
def write_to_csv(data):
    file = open("output.csv", "w", newline='', encoding="utf-8")
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()

# Запись в файл JSON
def write_to_json(data):
    file = open("output.json", "w", encoding="utf-8")
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.close()

# Подсчет бонуса для программистов
def calculate_programmer_bonus(employee):
    if employee[1] in ["Старший программист", "Ведущий программист", "Младший программист"]:
        return round(employee[3] * 0.03, 2)
    else:
        return 0

# Подсчет бонуса ко Дню защитника/8 марта
def calculate_sex_bonus(employee):
    if employee[0].startswith(("Сорокина", "Корнеева", "Савченко")):
        return 2000
    elif employee[0].startswith(("Иванов", "Струков", "Старчиков", "Бутенко")):
        return 2000
    else:
        return 0

# Подсчет индексации зарплаты
def calculate_salary_increase(employee):
    hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
    years_worked = (datetime.now() - hire_date).days / 365
    if years_worked > 10:
        return round(employee[3] * 0.07, 2)
    else:
        return round(employee[3] * 0.05, 2)

# Список сотрудников для графика отпусков
def vacation_list(employees):
    vacation_people = []
    for employee in employees[1:]:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
        months_worked = (datetime.now() - hire_date).days / 30
        if months_worked > 6:
            vacation_people.append(employee[0])
    return vacation_people

# Обработка сотрудников
def process_employees(employees):
    for employee in employees[1:]:
        programmer_bonus = calculate_programmer_bonus(employee)
        sex_bonus = calculate_sex_bonus(employee)
        salary_increase = calculate_salary_increase(employee)

        print(employee[0], ":")
        print("  Премия ко Дню программиста:", programmer_bonus, "рублей.")
        print("  Премия на 8 марта/23 февраля:", sex_bonus, "рублей.")
        print("  Индексация зарплаты:", salary_increase, "рублей.\n")

    vacation_employees = vacation_list(employees)
    print("Сотрудники, которые могут уйти в отпуск:", vacation_employees)

    write_to_csv(employees)
    write_to_json(employees)

process_employees(employees)