import csv
from datetime import datetime,timedelta

names=[]
job_titles=[]
work_time=[]
payroll=[]

with open('payroll.csv',newline='') as payroll_csv:
          payroll_reader=csv.DictReader(payroll_csv,delimiter=';')
          for row in payroll_reader:
            names.append(row['ФИО'])
            job_titles.append(row['Должность'])
            work_time.append(row['Дата найма'])
            payroll.append(row['Оклад'])

#создание словаря строк
data = []
for i in range(len(names)):
      data.append({
        'ФИО': names[i],
        'Должность': job_titles[i],
        'Дата найма': work_time[i],
        'Оклад': payroll[i]
    })
      

#увелечение оклада программистам
def increase_payroll_for_programmers(data):
    updated_data = []
    for row in data:
        if 'программист' in row['Должность']:
            row['Оклад']=float(row['Оклад'])*1.03
        updated_data.append({
            'ФИО': row['ФИО'],
            'Должность': row['Должность'],
            'Оклад': row['Оклад']
        })
    return updated_data
    
bonus_programmers=increase_payroll_for_programmers(data)
print("Премии программистам:")
print(bonus_programmers)


#выплата к 8 марта и 23 февраля
def pay_bonus_for_holidays(data):
    updated_data = []
    for row in data:
        row['Оклад'] = float(row['Оклад']) + 2000
        updated_data.append({
            'ФИО': row['ФИО'],
            'Должность': row['Должность'],
            'Оклад': row['Оклад']
        })
    return updated_data

holiday_bonus=pay_bonus_for_holidays(data)
print("Праздничные премии:")
print(holiday_bonus)


#индексация зарплат >10 лет 7%, остальным - 5%
def index_of_payroll(data):
    updated_data = []
    current_date = datetime.today()
    
    for row in data:
        if ((current_date - datetime.strptime(row['Дата найма'], "%d.%m.%Y")).days / 365) > 10:
            row['Оклад'] = float(row['Оклад']) * 1.07
        else:
            row['Оклад'] = float(row['Оклад']) * 1.05
        
        updated_data.append({
            'ФИО': row['ФИО'],
            'Должность': row['Должность'],
            'Оклад': row['Оклад']
        })
    return updated_data

index=index_of_payroll(data)
print("Индексация зарплаты:")
print(index)


#список отпусков (>6 месяцев отработали)
def vacation_list(data):
    vacation = []
    current_date = datetime.today()
    
    for row in data:
        if ((current_date - datetime.strptime(row['Дата найма'], "%d.%m.%Y")).days) > 183:
            vacation.append({
                'ФИО': row['ФИО'],
                'Должность': row['Должность']
            })
        
    return vacation
       
vacation = vacation_list(data)
print("Список сотрудников с отпусками:")
print(vacation)

def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()  
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()  
        for row in data:
            writer.writerow(row)      

# сохраняем данные после увеличения оклада программистам
bonus_programmers = increase_payroll_for_programmers(data)
write_to_csv(bonus_programmers, 'bonus_programmers.csv')

# сохраняем праздничные премии
holiday_bonus = pay_bonus_for_holidays(data)
write_to_csv(holiday_bonus, 'holiday_bonus.csv')

# сохраняем индексацию зарплат
index = index_of_payroll(data)
write_to_csv(index, 'indexed_salaries.csv')

# сохраняем список отпусков
vacation = vacation_list(data)
write_to_csv(vacation, 'vacation_list.csv')
