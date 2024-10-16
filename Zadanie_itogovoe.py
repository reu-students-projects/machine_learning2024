import csv
import json
from datetime import datetime
from typing import List

employees_data = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000],
]

def calculate_programmer_bonus(salary: int) -> float:
    return salary * 0.03

def calculate_gender_bonus(fio: str) -> int:
    if 'ж' in fio.lower():  
        return 2000  # Премия к 8 марта
    return 2000  # Премия к 23 февраля

def index_salary(hire_date: str, salary: int) -> float:
    hire_date_dt = datetime.strptime(hire_date, "%d.%m.%Y")
    years_worked = (datetime.now() - hire_date_dt).days // 365
    if years_worked > 10:
        return salary * 1.07  # 7%
    return salary * 1.05  # 5%

def get_employees_on_leave(employees: List[List]) -> List[str]:
    eligible_employees = []
    for emp in employees:
        hire_date_dt = datetime.strptime(emp[2], "%d.%m.%Y")
        months_worked = (datetime.now() - hire_date_dt).days // 30
        if months_worked > 6:
            eligible_employees.append(emp[0])
    return eligible_employees

def write_to_csv(filename: str, employees: List[List]) -> None:
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ФИО', 'Должность', 'Дата найма', 'Оклад'])
        writer.writerows(employees)

def write_to_json(filename: str, employees: List[List]) -> None:
    json_data = [
        {'ФИО': emp[0], 'Должность': emp[1], 'Дата найма': emp[2], 'Оклад': emp[3]}
        for emp in employees
    ]
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Расчет и вывод премий
    print("Премии программистов:")
    for emp in employees_data:
        if 'программист' in emp[1].lower():
            bonus = calculate_programmer_bonus(emp[3])
            print(f"{emp[0]}: {bonus:.2f}")

    print("\nГендерные премии:")
    for emp in employees_data:
        bonus = calculate_gender_bonus(emp[0])
        print(f"{emp[0]} получает {bonus} к празднику")

    # Индексация зарплат
    print("\nИндексация зарплат:")
    for emp in employees_data:
        new_salary = index_salary(emp[2], emp[3])
        print(f"{emp[0]}: новая зарплата {new_salary:.2f}")

    # Список сотрудников в отпуск
    eligible_employees = get_employees_on_leave(employees_data)
    print("\nСотрудники, отработавшие более 6 месяцев:")
    for employee in eligible_employees:
        print(employee)

    write_to_csv("employees.csv", employees_data)
    print("\nДанные сотрудников записаны в файл employees.csv")

    write_to_json("employees.json", employees_data)
    print("Данные сотрудников записаны в файл employees.json")

