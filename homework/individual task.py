import csv
import json
import datetime


employees_data = []
    
with open('employees.csv', newline='') as employees_csv:
    employees_reader = csv.DictReader(employees_csv, delimiter = ';')
    for row in employees_reader:
    	employees_data.append(row)
    for row in employees_data:
        row.update({'Дата найма': datetime.datetime(int(row['Дата найма'].split('.')[2]), int(row['Дата найма'].split('.')[1]), int(row['Дата найма'].split('.')[0]))})
        row.update({'Оклад': int(row['Оклад'].replace(' ', ''))})


#=== просто отделяющая граница
def border ():
    return '\n' + '='*30 + '\n' + '='*30 + '\n'


#=== меню (выбор функции + продолжение/завершение программы)
def menu ():
    print(border() + '\nВыберите необходимое действие:\n')
    print('1) Рассчитать премию сотрудников ко дню программиста')
    print('2) Рассчитать премию к 8 марта и к 23 февраля')
    print('3) Рассчитать индексированную зарплату')
    print('4) Вывести список сотрудников, отработавших в компании более 6 месяцев\n')
    function = input('Введите номер необходимой функции: ')
    match function:
        case '1':
            programmer_day_bonus(employees_data)
        case '2':
            holiday_bonus(employees_data)
        case '3':
            indexed_salaries(employees_data)
        case '4':
            six_months_plus(employees_data)
        case _:
            print('\nНеверное значение. Попробуйте еще раз')
            menu()
    print(border())
    cont = input('Чтобы продолжить нажмите "1", чтобы выйти из программы нажмите любую другую клавишу: ')
    if cont == '1':
        menu()
    else:
        print('\n      Хорошего дня!\n\n*★,°*:.☆(￣▽￣)/$:*.°★*') 


def csv_writer (list_):
    with open('output.csv', 'w') as output_csv:
    	output_writer = csv.DictWriter(output_csv, fieldnames=list_[0].keys())
    	output_writer.writeheader()
    	for item in list_:
    		output_writer.writerow(item)


def json_writer (list_):
    with open('output.json', 'w') as json_file:
	    json.dump(list_, json_file, ensure_ascii=False, indent=4)


#=== нужно ли записывать результаты в файл + в каком формате
def to_write_or_not_to_write(list_, if_function2=[]):
    print(border() + f'\nВы хотите записать результат в файл "{new_file_name}"?\nда - 1\nнет - любая другая клавиша')
    write = input()
    if write == '1':
        print('\nКакой формат файла вам нужен?\n0 - .csv\n1 - .json')
        file_format = input()
        match file_format:
            case '0':
                csv_writer(list_)
                if if_function2:
                    csv_writer(if_function2)
                print('\nЗапись завершена!')
            case '1':
                json_writer(list_)
                if if_function2:
                    json_writer(if_function2)
                print('\nЗапись завершена!')
            case _:
                print('\nНеверное значение. Попробуйте еще раз')
                to_write_or_not_to_write(list_)


#=== расчет премий на день программиста
def programmer_day_bonus (employees_data):
    programmer_day_bonus = []
    for row in employees_data:
        employee = {}
        employee.update({'ФИО': row['ФИО'], 'Премия': row['Оклад'] * 0.03})
        programmer_day_bonus.append(employee)
    print(border() + '\n' + 'Премии ко дню программиста:\n')
    for row in programmer_day_bonus:
        print(row['ФИО'] + ' - ' + str(row['Премия']))
    to_write_or_not_to_write(programmer_day_bonus)

    
#=== расчет премий на 8 марта/23 февраля
def holiday_bonus (employees_data):
    women_bonuses = []
    men_bonuses = []
    for row in employees_data:
        women = {}
        men = {}
        if row['Пол'] == 'Ж':
            women.update({'ФИО': row['ФИО'], 'Премия': 2000})
            women_bonuses.append(women)
        else:
            men.update({'ФИО': row['ФИО'], 'Премия': 2000})
            men_bonuses.append(men)
    print(border() + '\n' + 'Премии на 8 марта:\n')
    for row in women_bonuses:
        print(row['ФИО'] + ' - ' + str(row['Премия']))
    print('\n\n' + 'Премии на 23 февраля:\n')
    for row in men_bonuses:
        print(row['ФИО'] + ' - ' + str(row['Премия']))
    to_write_or_not_to_write(women_bonuses, men_bonuses)


#=== расчет проиндексированных зарплат
def indexed_salaries (employees_data):
    employees_bonuses = []
    today = datetime.datetime.now()
    for row in employees_data:
        indexed_salaries = {}
        difference = (today - row['Дата найма'])
        dif_years = difference.days / 365
        if dif_years > 10:
            indexed_salaries.update({'ФИО': row['ФИО'], 'Проиндексированная зарплата': round(row['Оклад'] * 1.07, ndigits=2)})
            employees_bonuses.append(indexed_salaries)
        else:
            indexed_salaries.update({'ФИО': row['ФИО'], 'Проиндексированная зарплата': round(row['Оклад'] * 1.07, ndigits=2)})
            employees_bonuses.append(indexed_salaries)
    print(border() + '\nПроиндексированные зарплаты:\n')
    for row in employees_bonuses:
        print(row['ФИО'] + ' - ' + str(row['Проиндексированная зарплата']))
    to_write_or_not_to_write(employees_bonuses)
    

#=== список сотрудников, отработавших более 6 месяцев
def six_months_plus(employees_data):
    employees = []
    today = datetime.datetime.now()
    for row in employees_data:
        employees_dict = {}
        difference = today - row['Дата найма']
        dif_months = difference.days / 31
        if dif_months > 6:
            employees_dict.update({'ФИО': row['ФИО']})
            employees.append(employees_dict)
    print(border() + '\nСотрудники, отработавшие более 6 месяцев:\n')
    for row in employees:
        print(row['ФИО'])


#=== ввод названия файла для записи + вызов меню
new_file_name = input('Введите название файла для записи данных: ')
menu()