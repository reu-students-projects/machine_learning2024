import csv
import json
from datetime import datetime

big_list = [{'ФИО': 'Иванов Иван Иванович', 'Должность': 'Менеджер', 'Дата найма': '22.10.2013', 'Оклад': 250000},
            {'ФИО': 'Сорокина Екатерина Матвеевна', 'Должность': 'Аналитик', 'Дата найма': '12.03.2020', 'Оклад': 75000},
            {'ФИО': 'Струков Иван Сергеевич', 'Должность': 'Старший программист', 'Дата найма': '23.04.2012', 'Оклад': 150000},
            {'ФИО': 'Корнеева Анна Игоревна', 'Должность': 'Ведущий программист', 'Дата найма': '22.02.2015', 'Оклад': 120000},
            {'ФИО': 'Старчиков Сергей Анатольевич', 'Должность': 'Младший программист', 'Дата найма': '12.11.2021', 'Оклад': 50000},
            {'ФИО': 'Бутенко Артем Андреевич', 'Должность': 'Архитектор', 'Дата найма': '12.02.2010', 'Оклад': 200000},
            {'ФИО': 'Савченко Алина Сергеевна', 'Должность': 'Старший аналитик', 'Дата найма': '13.04.2016', 'Оклад': 100000}]

results = []

with open('employees.csv', 'w') as employees:
    fields = ['ФИО', 'Должность', 'Дата найма', 'Оклад']
    writer = csv.DictWriter(employees, fieldnames = fields)
    writer.writeheader()
    writer.writerows(big_list)

def calculate_programmer_bonus():
    with open('employees.csv', newline='') as employees_csv:
        employee_reader = csv.DictReader(employees_csv)
        for row in employee_reader:
            salary = int(row['Оклад'])
            if 'программист' in row['Должность']:
                bonus = salary * 0.03
            else:
                bonus = 0
            row['Премия ко дню программиста'] = bonus
            results.append(row)

def calculate_holiday_bonus():
    for row in results:
        fio = row['ФИО']
        if fio.split()[1].endswith('а'):
            bonus = 2000
        else:
            bonus = 2000
        row['Премия к праздникам'] = bonus


def calculate_salary_indexation():
    for row in results:
        date = datetime.strptime(row['Дата найма'], '%d.%m.%Y')
        current_date = datetime.now()
        salary = int(row['Оклад'])
        years_worked = (current_date - date).days // 365
        if years_worked > 10:
            new_salary = salary * 1.07
        else:
            new_salary = salary * 1.05
        row['Индексированная зарплата'] = new_salary

def vacation_schedule():
    current_date = datetime.now()
    for row in results:
        date = datetime.strptime(row['Дата найма'], '%d.%m.%Y')
        months_worked = (current_date - date).days // 30
        if months_worked > 6:
            row['Право на отпуск'] = 'Да'  # Если больше 6 месяцев, право на отпуск
        else:
            row['Право на отпуск'] = 'Нет'

calculate_programmer_bonus()
calculate_holiday_bonus()
calculate_salary_indexation()
vacation_schedule()

with open('final_results.csv', 'w') as output_csv:
    fields = ['ФИО', 'Должность', 'Дата найма', 'Оклад', 'Премия ко дню программиста', 'Премия к праздникам',
              'Индексированная зарплата', 'Право на отпуск']
    writer = csv.DictWriter(output_csv, fieldnames=fields)
    writer.writeheader()
    for item in results:
        writer.writerow(item)

print("Данные успешно записаны в 'final_results.csv'")

with open('final_results.json', 'w') as output_json:
    json.dump(results, output_json)

print("Данные успешно записаны в 'final_results.json'")