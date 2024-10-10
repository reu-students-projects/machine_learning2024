import csv
from datetime import datetime
import json

employees = [
    ["ФИО", "Должность", "Дата найма", "Оклад", "Пол"],
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", "250000", "Мужской"],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", "75000", "Женский"],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", "150000", "Мужской"],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", "120000", "Женский"],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", "50000", "Мужской"],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", "200000", "Мужской"],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", "100000", "Женский"]
]


def write_to_csv(filename, data): # Создание CSV файла
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
def write_to_json(filename, data): # Создание Json файла
    
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    

def calc_premia(salary):  # Задание 1
    premia = salary * 0.03
    return premia 

premias = {}  # Словарь, где ключ будет ФИО, а значение - премия

def calc_gender_premia(gender, current_date):  # Задание 2
    if gender == 'Женский' and current_date.month == 3 and current_date.day == 8:
        return 2000
    elif gender == 'Мужской' and current_date.month == 2 and current_date.day == 23:
        return 2000
    else: 
        return 0

gender_premias = {}  # Словарь для задания 2
current_date = datetime.now()  # Получение текущей даты

def calc_indexation(hire_date, salary):  # Задание 3
    hire_date_obj = datetime.strptime(hire_date, "%d.%m.%Y")  # Формат
    years_worked = (datetime.now() - hire_date_obj).days // 365  # Сколько лет работал
    if years_worked > 10:
        return salary * 0.07
    else:
        return salary * 0.05

salary_indexations = {}  # Словарь для задания 3

def get_vacation_eligible_employees(employees_data, current_date):
    eligible_employees = []

    for employee in employees_data:
        hire_date_obj = datetime.strptime(employee[2], "%d.%m.%Y")  # Дата найма
        months_difference = (current_date.year - hire_date_obj.year) * 12 + (current_date.month - hire_date_obj.month)
        
        if months_difference > 6:
            eligible_employees.append(employee[0])  # Добавляем ФИО

    return eligible_employees

write_to_csv('employees.csv', employees)
# Основной код
with open('employees.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    employee_data = [list(row.values()) for row in reader]  # Сохраняем только данные сотрудников
    for row in employee_data:
        salary = int(row[3])  # Оклад
        position = row[1]  # Должность
        gender = row[4]  # Пол
        hire_date = row[2]  # Дата найма
        
        
        gender_premia = calc_gender_premia(gender, current_date)
        gender_premias[row[0]] = gender_premia

        
        indexation = calc_indexation(hire_date, salary)
        salary_indexations[row[0]] = indexation

        
        if 'программист' in position:
            premia = calc_premia(salary)
            premias[row[0]] = premia

# Вывод для задания 1
for name, premia in premias.items():
    print(f"{name} - Премия = {premia:.2f}") 

print("\n")

# Вывод для задания 2
for name, gender_premia in gender_premias.items(): 
    print(f"{name} - Премия = {gender_premia:.2f}")

print("\n")

# Вывод для задания 3
for name, indexation in salary_indexations.items():
    print(f"{name} - Индексация = {indexation:.2f}")

print("\n")

# Вывод для задания 4
eligible_employees = get_vacation_eligible_employees(employee_data, current_date)
for employee in eligible_employees:
    print(employee)

json_data = [dict(zip(employees[0], employee)) for employee in employees[1:]]  # Преобразование в формат для JSON
write_to_json('employees.json', json_data)  # Запись в JSON файл