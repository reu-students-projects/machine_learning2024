import csv
import datetime
from datetime import timedelta
import json

values = [{'ФИО': 'Иванов Иван Иванович', 'Должность': 'Менеджер', 'Дата найма': '22.10.2013', 'Оклад': 250000},
          {'ФИО': 'Сорокина Екатерина Матвеевна', 'Должность': 'Аналитик', 'Дата найма': '12.03.2020', 'Оклад': 75000},
          {'ФИО': 'Струков Иван Сергеевич', 'Должность': 'Старший программист', 'Дата найма': '23.04.2012', 'Оклад': 150000},
          {'ФИО': 'Корнеева Анна Игоревна', 'Должность': 'Ведущий программист', 'Дата найма': '22.05.2015', 'Оклад': 120000},
          {'ФИО': 'Старчиков Сергей Анатольевич', 'Должность': 'Младший программист', 'Дата найма': '12.11.2021', 'Оклад': 50000},
          {'ФИО': 'Бутенко Артем Андреевич', 'Должность': 'Архитектор', 'Дата найма': '12.02.2010', 'Оклад': 200000},
          {'ФИО': 'Савченко Алина Сергевна', 'Должность': 'Старший аналитик', 'Дата найма': '13.04.2016', 'Оклад': 100000}]

#создание файла и запись исходных данных
with open('file.csv', 'w', newline='') as file_csv:
    fields = ['ФИО', 'Должность', 'Дата найма', 'Оклад']
    file_writer = csv.DictWriter(file_csv, fieldnames=fields, delimiter=';')
    file_writer.writeheader()
    for item in values:
        file_writer.writerow(item)


#функция, рассчитывающая премию для программистов
def bonus():
    bonus_dict = {}
    with open('file.csv', newline="") as file_csv:
        position_reader = csv.DictReader(file_csv, delimiter=';')
        for row in position_reader:
            if 'программист' in row['Должность']:
                bonus_dict[row['ФИО']] = float(row['Оклад']) * 0.03
    return bonus_dict


#премия к праздникам
def holiday_bonus():
    return 2000


#индексация зарплат
def new_salary ():
    new_salary_dict = {}
    with open('file.csv', newline="") as file_csv:
        date_reader = csv.DictReader(file_csv, delimiter=';')
        for row in date_reader:
            today = datetime.date.today()
            date_hiring = datetime.datetime.strptime(row['Дата найма'], '%d.%m.%Y').date()
            if today-date_hiring >= timedelta(days=3650):
                new_salary_dict[row['ФИО']] = float(row['Оклад']) * 0.07 + float(row['Оклад'])
            else: new_salary_dict[row['ФИО']] = float(row['Оклад']) * 0.05 + float(row['Оклад'])
    return new_salary_dict


#функция, находящая сотрудников, которые отработали более 6 месяцев (для графика отпусков)
def on_vacation():
    on_vacation_list = []
    with open('file.csv', newline="") as file_csv:
        date_reader = csv.DictReader(file_csv, delimiter=';')
        for row in date_reader:
            today = datetime.date.today()
            date_hiring = datetime.datetime.strptime(row['Дата найма'], '%d.%m.%Y').date()
            if today - date_hiring >= timedelta(days=180):
                on_vacation_list.append(row['ФИО'])
        return on_vacation_list

BonusDict = bonus()
NewSalaryDict = new_salary()

#добавление новых столбцов с данными
def into_csv():
    with open('file.csv', newline='') as file_csv:
        file_reader = csv.DictReader(file_csv, delimiter=';')
        rows = [row for row in file_reader]
        for row in rows:
            name = row['ФИО']
            row['Премия'] = BonusDict.get(name, 0)
            row['Премия к празднику'] = holiday_bonus()
            row['Индексированная зарплата'] = NewSalaryDict.get(name, row['Оклад'])
    with open('file.csv', 'w', newline='') as file_csv:
        fields = file_reader.fieldnames + ['Премия', 'Премия к празднику', 'Индексированная зарплата']
        file_writer = csv.DictWriter(file_csv, fieldnames=fields, delimiter=';')
        file_writer.writeheader()
        file_writer.writerows(rows)

    with open('file.csv', 'a', newline='') as file_csv:
        file_writer = csv.writer(file_csv, delimiter=';')
        file_writer.writerow({})
        file_writer.writerow(['Сотрудники, которым пора в отпуск'])
        for item in on_vacation():
            file_writer.writerow([item])
    return "Запись в csv-файл прошла успешно"

#запись в json
def into_json():
    with open('file.json', 'w', encoding='utf-8') as json_file:
        json.dump(values, json_file, ensure_ascii=False)

    with open('file.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for row in data:
            name = row['ФИО']
            row['Премия'] = BonusDict.get(name, 0)
            row['Премия к празднику'] = holiday_bonus()
            row['Индексированная зарплата'] = NewSalaryDict.get(name, row['Оклад'])

    with open('file.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
    return "Запись в json-файл прошла успешно"

print(into_csv())
print(into_json())