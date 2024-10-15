import csv
import json
from datetime import datetime, date
from typing import List
import matplotlib.pyplot as plt

class Employee:
    def __init__(self, last_name, first_name, middle_name, position, hire_date_str, salary):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__position = position
        self.__hire_date = datetime.strptime(hire_date_str, "%d.%m.%Y").date()
        self.__salary = salary

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_position(self):
        return self.__position

    def get_hire_date(self):
        return self.__hire_date

    def get_salary(self):
        return self.__salary

    def set_last_name(self, value):
        self.__last_name = value

    def set_first_name(self, value):
        self.__first_name = value

    def set_middle_name(self, value):
        self.__middle_name = value

    def set_position(self, value):
        self.__position = value

    def set_hire_date(self, value):
        self.__hire_date = datetime.strptime(value, "%d.%m.%Y").date()

    def set_salary(self, value):
        self.__salary = value

    def calculate_programmers_day_bonus(self):
        """Считаем 3% бонус для программистов"""
        if 'программист' in self.__position.lower():
            bonus = self.__salary * 0.03
            return bonus
        else:
            return 0

    def is_female(self):
        """Определяем пол по окончанию"""
        return self.__middle_name.endswith('на')

    def calculate_gender_holiday_bonus(self):
        """Считаем бонус для праздника мужчин/женщин"""
        bonus = 2000
        return bonus

    def calculate_salary_indexation(self):
        """Индексация зарплат"""
        years_worked = (date.today() - self.__hire_date).days / 365.25
        if years_worked > 10:
            increase = self.__salary * 0.07
        else:
            increase = self.__salary * 0.05
        self.__salary += increase
        return increase

    def eligible_for_vacation(self):
        """Проверка на длительность работы более 6 месяцев"""
        months_worked = (date.today() - self.__hire_date).days / 30.44
        return months_worked >= 6

    def calculate_tax_deductions(self):
        """Налоги"""
        income_tax = self.__salary * 0.13
        social_insurance = self.__salary * 0.015
        return {'income_tax': income_tax, 'social_insurance': social_insurance}

    def to_dict(self):
        """Конвертиуем в словарь"""
        return {
            'Фамилия': self.__last_name,
            'Имя': self.__first_name,
            'Отчество': self.__middle_name,
            'Должность': self.__position,
            'Дата найма': self.__hire_date.strftime("%d.%m.%Y"),
            'Оклад': self.__salary
        }

# List of employees based on provided data
employees = [
    Employee('Иванов', 'Иван', 'Иванович', 'Менеджер', '22.10.2013', 250000),
    Employee('Сорокина', 'Екатерина', 'Матвеевна', 'Аналитик', '12.03.2020', 75000),
    Employee('Струков', 'Иван', 'Сергеевич', 'Старший программист', '23.04.2012', 150000),
    Employee('Корнеева', 'Анна', 'Игоревна', 'Ведущий программист', '22.02.2015', 120000),
    Employee('Старчиков', 'Сергей', 'Анатольевич', 'Младший программист', '12.11.2021', 50000),
    Employee('Бутенко', 'Артем', 'Андреевич', 'Архитектор', '12.02.2010', 200000),
    Employee('Савченко', 'Алина', 'Сергеевна', 'Старший аналитик', '13.04.2016', 100000),
]

def calculate_wage_fund(employees: List[Employee]):
    total_salary = sum(emp.get_salary() for emp in employees)
    return total_salary

def plot_salaries_by_position(employees: List[Employee]):
    positions = {}
    for emp in employees:
        position = emp.get_position()
        salary = emp.get_salary()
        if position in positions:
            positions[position] += salary
        else:
            positions[position] = salary

    positions_list = list(positions.keys())
    salaries = list(positions.values())

    plt.bar(positions_list, salaries)
    plt.xlabel('Должность')
    plt.ylabel('Суммарный оклад')
    plt.title('Суммарные оклады по должностям')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def write_to_csv(employees: List[Employee], filename='employees.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Фамилия', 'Имя', 'Отчество', 'Должность', 'Дата найма', 'Оклад']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for emp in employees:
            writer.writerow(emp.to_dict())

def write_to_json(employees: List[Employee], filename='employees.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([emp.to_dict() for emp in employees], file, ensure_ascii=False, indent=4)

def get_vacation_schedule(employees: List[Employee]):
    eligible_employees = [emp for emp in employees if emp.eligible_for_vacation()]
    return eligible_employees

if __name__=='__main__':
    total_wage_fund = calculate_wage_fund(employees)
    print(f"Фонд оплаты труда: {total_wage_fund} руб.")

    plot_salaries_by_position(employees)
    write_to_csv(employees)
    write_to_json(employees)

    def calculate_programmers_day_total_bonus(employees: List[Employee]):
        total_bonus = sum(emp.calculate_programmers_day_bonus() for emp in employees)
        return total_bonus

    total_programmers_bonus = calculate_programmers_day_total_bonus(employees)
    print(f"Общая премия ко Дню программиста: {total_programmers_bonus} руб.")

    def calculate_gender_holiday_bonuses(employees: List[Employee]):
        total_bonus = sum(emp.calculate_gender_holiday_bonus() for emp in employees)
        return total_bonus

    total_gender_bonus = calculate_gender_holiday_bonuses(employees)
    print(f"Общая премия к гендерным праздникам: {total_gender_bonus} руб.")

    def apply_salary_indexation(employees: List[Employee]):
        for emp in employees:
            increase = emp.calculate_salary_indexation()
            print(f"{emp.get_last_name()} {emp.get_first_name()}: Индексация оклада на {increase} руб.")

    apply_salary_indexation(employees)

    vacation_schedule = get_vacation_schedule(employees)
    print("Сотрудники, имеющие право на отпуск:")
    for emp in vacation_schedule:
        print(f"{emp.get_last_name()} {emp.get_first_name()}")

    for emp in employees:
        taxes = emp.calculate_tax_deductions()
        print(f"{emp.get_last_name()} {emp.get_first_name()}: НДФЛ - {taxes['income_tax']} руб., Соц. страхование - {taxes['social_insurance']} руб.")
