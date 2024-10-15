import csv
import json
from datetime import datetime

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

def write_to_csv(data, filename="output.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def write_to_json(data, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def calculate_programmer_bonus(employee):
    programmers_positions = ["Старший программист", "Ведущий программист", "Младший программист"]
    if employee[1] in programmers_positions:
        return round(employee[3] * 0.03, 2)  
    return 0


def calculate_gender_bonus(employee):
    if "Сорокина" in employee[0] or "Корнеева" in employee[0] or "Савченко" in employee[0]:
        return 2000
    if "Иванов" in employee[0] or "Струков" in employee[0] or "Старчиков" in employee[0] or "Бутенко" in employee[0]:
        return 2000
    return 0

def calculate_salary_increase(employee):
    hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
    years_worked = (datetime.now() - hire_date).days / 365
    if years_worked > 10:
        return round(employee[3] * 0.07, 2)  # 7% индексация
    return round(employee[3] * 0.05, 2)  # 5% индексация

def vacation_list(employees):
    eligible_for_vacation = []
    for employee in employees[1:]:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
        months_worked = (datetime.now() - hire_date).days / 30
        if months_worked > 6:
            eligible_for_vacation.append(employee[0])
    return eligible_for_vacation

def process_employees(employees):
    for employee in employees[1:]:
        programmer_bonus = calculate_programmer_bonus(employee)
        gender_bonus = calculate_gender_bonus(employee)
        salary_increase = calculate_salary_increase(employee)
        
        print(f"{employee[0]}:")
        print(f"  Премия ко Дню программиста: {programmer_bonus} рублей.")
        print(f"  Премия на 8 марта/23 февраля: {gender_bonus} рублей.")
        print(f"  Индексация зарплаты: {salary_increase} рублей.\n")
    
    vacation_employees = vacation_list(employees)
    print("Сотрудники, eligible для отпуска:", vacation_employees)
    
    write_to_csv(employees)
    write_to_json(employees)

process_employees(employees)