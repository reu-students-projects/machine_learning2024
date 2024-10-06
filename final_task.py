import csv
import json
from datetime import datetime

employees = []
bonus_percentage = 0.03
holiday_bonus = 2000
index_long = 0.07
index_standard = 0.05
employees_6_months = []

def calculate_bonus():
    with open('employees.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        
        for row in reader:
            position = row['Должность']
            salary = row['Оклад'].replace(' ', '')
            salary = int(salary)

            hire_date_str = row['Дата принятия']
            hire_date = datetime.strptime(hire_date_str, "%d.%m.%Y")
            years_of_work = (datetime.now() - hire_date).days // 365
            months_of_work = (datetime.now() - hire_date).days // 30
            
            programmer_bonus = salary * bonus_percentage if 'программист' in position.lower() else 0
            
            after_index = salary + salary * (index_long if years_of_work > 10 else index_standard)
            
            total_bonus = programmer_bonus + holiday_bonus + after_index
            
            employee_data = {
                'ФИО': row['ФИО'],
                'Оклад': salary,
                'Премия для программистов': round(programmer_bonus, 2),
                'Праздничная премия': round(holiday_bonus, 2),
                'Оклад после индексации': round(after_index, 2),
                'Общая премия': round(total_bonus, 2)
            }
            employees.append(employee_data)

            if months_of_work > 6:
                months_data = {
                    'ФИО': row['ФИО']
                }
                employees_6_months.append(months_data)

        for employee in employees:
            print(f"{employee['ФИО']}: Премия для программистов: {employee['Премия для программистов']}, "
                  f"Праздничная премия: {employee['Праздничная премия']}, "
                  f"Оклад после индексации: {employee['Оклад после индексации']}, "
                  f"Общая премия: {employee['Общая премия']}")
        
        print('Сотрудники, работающие более 6 месяцев: ')
        for emp in employees_6_months:
            print(f"{emp['ФИО']}")

    with open('output.csv', 'w', newline='', encoding='utf-8') as output_csv:
        fields = ['ФИО', 'Оклад', 'Премия для программистов', 'Праздничная премия', 'Оклад после индексации', 'Общая премия']
        output_writer = csv.DictWriter(output_csv, fieldnames=fields, delimiter=';')
        output_writer.writeheader()
        for item in employees:
            output_writer.writerow(item)
        
    with open('for_schedule.json', 'w', encoding='utf-8') as json_file:
        json.dump(employees_6_months, json_file, ensure_ascii=False, indent=4)

calculate_bonus()