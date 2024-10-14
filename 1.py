import csv
import json
from datetime import datetime
import matplotlib.pyplot as plt


class Employee:
    def __init__(self, last_name, first_name, middle_name, position, hire_date, salary):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__position = position
        self.__hire_date = hire_date
        self.__salary = salary

    # Геттеры и сеттеры для инкапсуляции
    def get_salary(self):
        return self.__salary

    def get_full_name(self):
        return self.__last_name + " " + self.__first_name + " " + self.__middle_name

    def get_position(self):
        return self.__position

    def get_hire_date(self):
        return self.__hire_date

    def set_salary(self, new_salary):
        self.__salary = new_salary

    # Метод для расчета премии
    def programmer_bonus(self):
        if 'программист' in self.__position.lower():
            return self.__salary * 0.03
        return 0

    # Бонус работникам на праздники
    def holiday_bonus(self):
        if 'а' in self.__middle_name[-1]:
            return print(f"Премия для {self.get_full_name()} (к 8 марта): 2000 рублей")
        else:
            return print(f"Премия для {self.get_full_name()} (к 23 марта): 2000 рублей")

    # Интексация
    def index_salary(self):
        hire_date = datetime.strptime(self.__hire_date, '%d.%m.%Y')
        time = (datetime.now() - hire_date).days / 365
        if time > 10:
            self.set_salary(self.get_salary() * 1.07)
            print(f"Увеличели на 7% {self.get_full_name()}: {self.get_salary()}")
        else:
            self.set_salary(self.get_salary() * 1.05)
            print(f"Увеличели на 5% {self.get_full_name()}: {self.get_salary()}")


    # Метод для расчета общего фонда оплаты труда
    @staticmethod
    def total_payroll(employees):
        return sum([employee.get_salary() for employee in employees])

    # Запись в JSON
    @staticmethod
    def save_to_json(filename, employees):
        json_data = [{"ФИО": employee.get_full_name(), "Должность": employee.get_position(),
                      "Дата найма": employee.get_hire_date(), "Оклад": employee.get_salary()} for
                     employee in employees]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def calculate_tax_deductions(employees):
        for employee in employees:
            income_tax =  sum([employee.get_salary() * 0.13 for employee in employees])
            social_security_rate = sum([employee.get_salary() * 0.3 for employee in employees])
        print('Подоходный налог: ', income_tax,"\nФонд социального страхования: ", social_security_rate, "\nОбщие отчисления: ", income_tax+social_security_rate)


employees_list = [
    Employee('Иванов', 'Иван', 'Иванович', 'Менеджер', '22.10.2013', 250000),
    Employee('Сорокина', 'Екатерина', 'Матвеевна', 'Аналитик', '12.03.2020', 75000),
    Employee('Струков', 'Иван', 'Сергеевич', 'Старший программист', '23.04.2012', 150000),
    Employee('Корнеева',  'Анна', 'Игоревна', 'Ведущий программист', '22.02.2015', 120000),
    Employee('Старчиков', 'Сергей', 'Анатольевич', 'Младший программист', '12.11.2021', 50000),
    Employee('Бутенко', 'Артем', 'Андреевич', 'Архитектор', '12.02.2010', 200000),
    Employee('Савченко', 'Алина', 'Сергеевна', 'Старший аналитик', '13.04.2016', 100000),
]

#Бонус работникам
for employee in employees_list:
    programmer_bon = Employee.programmer_bonus(employee)
    print(f"Бонус {Employee.get_full_name(employee)}: {programmer_bon}")

#Бонус работникам на праздники
for employee in employees_list:
    holiday_bon = Employee.holiday_bonus(employee)

# Интексация зарплаты
for employee in employees_list:
    Employee.index_salary(employee)

# фонд оплаты
total_pay = Employee.total_payroll(employees_list)

# Записываем данные сотрудников в JSON файл
Employee.save_to_json('employees.json', employees_list)

positions = [Employee.get_position(employee) for employee in employees_list]
salaries = [Employee.get_salary(employee) for employee in employees_list]

fig, ax = plt.subplots()
ax.bar(positions, salaries)
ax.set_ylabel('Зарплата (руб.)')
ax.set_title('Зарплата сотрудников по должностям')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(f"Фонд оплаты труда: {total_pay} рублей")

Employee.calculate_tax_deductions(employees_list)

