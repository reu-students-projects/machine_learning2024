import csv
import json
from datetime import datetime

employees = [
    ("Иван Сорокина", "Менеджер", "22.10.2013", "250000"),
    ("Струков Иван Старший", "Программист", "23.04.2012", "150000"),
    ("Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", "120000"),
    ("Стариков Анатольевич Младший", "Программист", "12.11.2021", "50000"),
    ("Бутенко Артем Андреевич", "Архитектор", "12.02.2010", "200000"),
    ("Савченко Алина Сергеевна Старший", "Аналитик", "13.04.2016", "100000")
]

def write_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ФИО", "Должность", "Дата найма", "Оклад"])
        for row in data:
            writer.writerow(row)

def calculate_bonus_programmer(salary):
    return salary * 0.03

def calculate_bonus_date(employee):
    name, position, hire_date, salary = employee
    salary = int(salary)
  
    if position.lower() == "программист" and datetime.now().month == 9:
        return calculate_bonus_programmer(salary)
    elif any(title in position.lower() for title in ["сотрудница", "аналитик"]) and datetime.now().month == 3:
        return 2000
    elif "программист" not in position.lower() and datetime.now().month == 2:
        return 2000
    return 0

def index_salary(employee):
    name, position, hire_date, salary = employee
    salary = int(salary)
    hire_date_obj = datetime.strptime(hire_date, "%d.%m.%Y")
    if (datetime.now() - hire_date_obj).days > 3650: 
        return salary * 0.07
    return salary * 0.05

def vacation_employees(employees):
    qualified = []
    for employee in employees:
        name, position, hire_date, _ = employee
        hire_date_obj = datetime.strptime(hire_date, "%d.%m.%Y")
        if (datetime.now() - hire_date_obj).days > 182: 
            qualified.append(employee)
    return qualified

def write_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    write_csv('employees.csv', employees)
    bonuses = {emp[0]: calculate_bonus_date(emp) for emp in employees}
    print("Премии по сотрудникам:")
    for name, bonus in bonuses.items():
        print(f"{name}: {bonus}")

    indexed_salaries = {emp[0]: index_salary(emp) for emp in employees}
    print("\nИндексация зарплат по сотрудникам:")
    for name, new_salary in indexed_salaries.items():
        print(f"{name}: {new_salary}")

    vacation_list = vacation_employees(employees)
    print("\nСотрудники, отработавшие более 6 месяцев:")
    for emp in vacation_list:
        print(emp[0])
    write_json('employees.json', employees)
