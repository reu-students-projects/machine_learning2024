import csv
import json
from datetime import datetime

# Чтение данных из CSV файла
def read_csv(file_name):
    employees = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовки
        for row in reader:
            row[5] = int(row[5])  # Преобразуем оклад в целое число
            employees.append(row)
    return employees

# 1. Функция для расчета премии программистам (3% от оклада)
def calculate_programmer_bonus(employees):
    bonus_percentage = 0.03
    bonuses = []
    for employee in employees:
        if "программист" in employee[3].lower():
            bonus = employee[5] * bonus_percentage
            bonuses.append(f"{employee[0]} {employee[1]}: Премия {bonus:.2f} рублей")
    return bonuses

# 2. Функция для расчета премии к 8 марта и 23 февраля
def calculate_gender_bonus(employees):
    march_bonus = 2000
    february_bonus = 2000
    bonuses = []
    for employee in employees:
        if employee[1].endswith('а'):  # Проверяем на женский пол по имени
            bonuses.append(f"{employee[0]} {employee[1]}: Премия к 8 марта {march_bonus} рублей")
        else:
            bonuses.append(f"{employee[0]} {employee[1]}: Премия к 23 февраля {february_bonus} рублей")
    return bonuses

# 3. Функция для индексации зарплат
def calculate_salary_indexation(employees):
    current_year = datetime.now().year
    new_salaries = []
    for employee in employees:
        hire_year = int(employee[4].split('.')[-1])
        years_worked = current_year - hire_year
        if years_worked > 10:
            indexation = 0.07
        else:
            indexation = 0.05
        new_salary = employee[5] * (1 + indexation)
        new_salaries.append(f"{employee[0]} {employee[1]}: Новая зарплата {new_salary:.2f} рублей")
    return new_salaries

# 4. Функция для составления графика отпусков (более 6 месяцев)
def get_employees_for_vacation(employees):
    current_date = datetime.now()
    vacation_list = []
    for employee in employees:
        hire_date = datetime.strptime(employee[4], "%d.%m.%Y")
        months_worked = (current_date.year - hire_date.year) * 12 + current_date.month - hire_date.month
        if months_worked > 6:
            vacation_list.append(f"{employee[0]} {employee[1]} {employee[2]}")
    return vacation_list

# 5. Функции записи в CSV и JSON
def write_to_csv(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия", "Имя", "Отчество", "Должность", "Дата найма", "Оклад"])  # Заголовки
        writer.writerows(data)

def write_to_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Чтение данных из CSV файла
employees = read_csv('machine_learning2024/final_task/employees.csv')

# Премии программистам
programmer_bonuses = calculate_programmer_bonus(employees)
print("Премии программистам:")
for bonus in programmer_bonuses:
    print(bonus)

# Премии к 8 марта и 23 февраля
gender_bonuses = calculate_gender_bonus(employees)
print("\nПремии к 8 марта и 23 февраля:")
for bonus in gender_bonuses:
    print(bonus)

# Индексация зарплат
new_salaries = calculate_salary_indexation(employees)
print("\nИндексация зарплат:")
for salary in new_salaries:
    print(salary)

# График отпусков
vacation_schedule = get_employees_for_vacation(employees)
print("\nГрафик отпусков:")
for employee in vacation_schedule:
    print(employee)

# Запись данных в CSV и JSON
write_to_csv('new_employees.csv', employees)
write_to_json('employees.json', employees)

print("\nДанные записаны в 'new_employees.csv' и 'employees.json'.")
