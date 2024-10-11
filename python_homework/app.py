from typing import List
from string import capwords
from texts import START_MSG, WRITE_FILE_MSG, MAN_WOMAN_PREM, TAXES_TEXT
from Employee import Employee
import csv, os, time, re, json

CSV_FILE_PATH = './task.csv' 

def read_employees_from_csv(file_path: str) -> List[Employee]:
    employees = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            name_parts = row[0].split()
            last_name = name_parts[0]
            first_name = name_parts[1]
            middle_name = name_parts[2] if len(name_parts) > 2 else None
            employee = Employee(
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                position=row[1],
                hire_date=Employee.parse_date(row[2]),
                salary=int(row[3].replace(' ', '')),
                sex=capwords(row[4])
            )
            employees.append(employee)
    return employees


def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
employees = read_employees_from_csv(CSV_FILE_PATH)
exit_flag = False

def write_to_file(file_type: str) -> bool:
    filename_flag = False
    clear()
    print(f"Выбрана запись в {file_type} файл")
    user_file_name = input("Введите имя файла без расширения (к примеру, employees): ")
    if user_file_name:
        filename_flag = True
        print(filename_flag)
        file_name = user_file_name + file_type
        if (file_type) == ".csv":
            Employee.write_to_csv(employees, f'csv/{file_name}')
        else:
            Employee.write_to_json(employees, f'json/{file_name}')
        clear()
        print(f'Файл записан в: {file_name}')
    else:
        print("Проверьте ввод")
        time.sleep(0.7)
    return filename_flag


def tax_parser(data: dict) -> str:
    MONTHS = ("январь", "февраль", "март", "апрель", "май", "июнь",
              "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь", "итого")
    text = ""
    for month, details in data.items():
        if month != 13:
            text +=\
f'''Данные на {MONTHS[month - 1]}:
    Оклад: {details['salary']}
    Премия: {details['premium']}
    Налоги
        НДФЛ: {details['taxes']['НДФЛ']}
        ФСС: {details['taxes']['ФСС']}
    Итоговая сумма на выплату работодателем за месяц: {details['month_sum']}
'''
        else:
            text += '-' * 40
            text += f"\nСумма всех выплат за год: {data[13]}\n"
    return text


while(not exit_flag):
    try:
        print(START_MSG)
        choose = input("Ваш выбор: ")
        if choose == '0':
            flag = False
            while(not flag):
                clear()
                print(WRITE_FILE_MSG)
                choose_write = input("Ваш выбор: ")
                if choose_write == '9': # назад
                    clear()
                    flag = True

                elif choose_write == '1': # json
                    filename_flag = False
                    while(not filename_flag):
                        filename_flag = write_to_file(".json")
                    flag = True

                elif choose_write == '2': # csv
                    filename_flag = False
                    while(not filename_flag):
                        filename_flag = write_to_file(".csv")
                    flag = True

                else:
                    print('Проверьте ввод')
                    time.sleep(0.7)
                    
        elif choose == '1': # Вывод текущих данных
            clear()
            for emp in employees:
                print(emp.print_everything, '\n')

        elif choose == '2': # Расчёт премии ко дню программиста
            for emp in employees:
                emp.prem_prog()
            clear()
            print('Программистам начислена премия')

        elif choose == '3': # Расчёт премии к 8 марта и 23 февраля
            clear()
            flag = False
            while(not flag):
                clear()
                print(MAN_WOMAN_PREM)
                choose_man_wom = input("Ваш выбор: ")
                if choose_man_wom == '9': # назад
                    clear()
                    flag = True
                elif choose_man_wom == '1': # 23.02
                    flag = True
                    for emp in employees:
                        emp.prem_man()
                    clear()
                    print('Начислены премии мужчинам')
                elif choose_man_wom == '2': # 8.03
                    flag = True
                    for emp in employees:
                        emp.prem_wom()
                    clear()
                    print('Начислены премии женщинам')
                else:
                    print('Проверьте ввод')
                    time.sleep(0.7)

        elif choose == '4': # Расчёт индексации зарплат
            for emp in employees:
                emp.index()
            clear()
            print("Зарплаты проиндексированы")

        elif choose == '5': # Получить список сотрудников, которым положен отпуск
            clear()
            print("Отпуск положен следующим сотрудникам:")
            for emp in employees:
                if emp.rest():
                    print("  ", emp.full_name)
            print()

        elif choose == '6': # Расчитать фонд оплаты труда
            clear()
            print(f"Годовой фонд оплаты труда: {Employee.wage_fund(employees)} рублей")

        elif choose == '7':
            clear()
            Employee.diagram(employees)

        elif choose == '8':
            clear()
            print(TAXES_TEXT)
            while(1):
                tax_choose = input("Ваш выбор: ")
                if tax_choose == '1':
                    clear()
                    print("Список сотрудников: ")
                    counter = 1
                    for emp in employees:
                        print(f'{counter}. {emp.full_name}')
                        counter += 1
                    while(1):
                        emp_choose = input("Выберите сотрудника (используйте номер из списка выше): ")
                        if re.fullmatch(r'\d+', emp_choose):
                            emp_choose = int(emp_choose)
                            if emp_choose > 0 and emp_choose <= counter:
                                clear()
                                taxes = Employee.taxes_counter(employees[emp_choose-1])
                                print(f'Для сотрудника {employees[emp_choose-1].full_name}:')
                                print(tax_parser(taxes))
                                print(\
f'''Желаете сохранить данные для "{employees[emp_choose-1].full_name}" в json файл?
    1. Да
    Нет - любое другое значение''')
                                save_choose = input('Ваш выбор: ')
                                if save_choose == '1':
                                    filename = input("Введите имя файла (без расширения), в который хотите сохранить результат: ")
                                    while not re.fullmatch(r'^(?!.*\.\.)(?!.*\.$)(?!^\.)(?!.*\/)(?!.*\\)[\w\-.]+$', 
                                                           filename):
                                        filename = input("Проверьте введое имя и повторите ввод: ")
                                    filepath = f'json/{filename}.json'
                                    emp_dict = {employees[emp_choose-1].full_name: taxes}
                                    with open(filepath, 'w', encoding='utf-8') as file:
                                        json.dump(emp_dict, fp=file, ensure_ascii=False, indent=4)
                                    clear()
                                    print(f'Данные по сотруднику "{employees[emp_choose-1].full_name}" успешно сохранены в: "{filepath}"\n')
                                else:
                                    clear()
                                break
                            else:
                                print("Проверьте ввод")
                        else:
                            print('Проверьте ввод')
                    break
                elif tax_choose == '2': # все в json
                    filename = input("Введите имя файла (без расширения), в который хотите сохранить результат: ")
                    while not re.fullmatch(r'^(?!.*\.\.)(?!.*\.$)(?!^\.)(?!.*\/)(?!.*\\)[\w\-.]+$', 
                                filename):
                        filename = input("Проверьте введое имя и повторите ввод: ")
                    filepath = f'json/{filename}.json'
                    emp_dict = {emp.full_name: Employee.taxes_counter(emp) for emp in employees}
                    with open(filepath, 'w', encoding='utf-8') as file:
                        json.dump(emp_dict, fp=file, ensure_ascii=False, indent=4)
                    clear()
                    print(f'Налоговые отчисления успешно сохранены в: {filepath}\n')
                    break                    
                elif tax_choose == '9':
                    clear()
                    break
                else:
                    print("Проверьте ввод")
            # дописать функционал: вывод списка сотрудников, сохранение json для всех сотрудников, сохранение json для конкретного сотрудника

        elif choose == '9': # Выход из программы
            exit_flag = True
        else:
            clear()
            print("Проверьте введённые данные")

    except ValueError: 
        clear()
        print('Проверьте ввод')

    except KeyboardInterrupt:
        exit_flag = True
        print()

    if exit_flag: 
        print('Выход из программы...')
        time.sleep(0.5)
        clear()
