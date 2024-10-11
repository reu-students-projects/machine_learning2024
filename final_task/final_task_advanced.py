import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Класс Employee с инкапсуляцией данных
class Employee:
    def __init__(self, last_name, first_name, middle_name, position, hire_date, salary):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__position = position
        self.__hire_date = datetime.strptime(hire_date, "%d.%m.%Y")
        self.__salary = salary

    # Геттеры
    def get_full_name(self):
        return f"{self.__last_name} {self.__first_name} {self.__middle_name}"

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    def get_hire_date(self):
        return self.__hire_date

    # Сеттеры
    def set_salary(self, new_salary):
        self.__salary = new_salary

    # Методы для расчета премий
    def calculate_programmer_bonus(self):
        if "программист" in self.__position.lower():
            return self.__salary * 0.03
        return 0

    def calculate_gender_bonus(self):
        if self.__first_name.endswith('а'):
            return 2000  # Премия к 8 марта
        return 2000  # Премия к 23 февраля

    # Метод для индексации зарплаты
    def calculate_salary_indexation(self):
        years_worked = datetime.now().year - self.__hire_date.year
        if years_worked > 10:
            indexation = 0.07
        else:
            indexation = 0.05
        self.__salary *= (1 + indexation)

    # Метод для проверки, может ли сотрудник пойти в отпуск
    def can_take_vacation(self):
        months_worked = (datetime.now().year - self.__hire_date.year) * 12 + (datetime.now().month - self.__hire_date.month)
        return months_worked > 6

# Чтение данных из CSV
def read_csv(file_name):
    employees = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            employees.append(Employee(row[0], row[1], row[2], row[3], row[4], int(row[5])))
    return employees

# Функция для расчета фонда оплаты труда
def calculate_payroll_fund(employees):
    total_fund = sum([employee.get_salary() for employee in employees])
    return total_fund

# Функция для построения диаграммы окладов по должностям
def plot_salary_distribution(employees):
    positions = {}
    for employee in employees:
        position = employee.get_position()
        salary = employee.get_salary()
        if position in positions:
            positions[position] += salary
        else:
            positions[position] = salary

    # Построение столбчатой диаграммы
    plt.bar(positions.keys(), positions.values())
    plt.xlabel('Должности')
    plt.ylabel('Оклад')
    plt.title('Распределение окладов по должностям')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Функция для расчета налоговых отчислений
def calculate_tax_deductions(employees):
    income_tax_rate = 0.13
    social_security_tax_rate = 0.3
    deductions = []

    for employee in employees:
        income_tax = employee.get_salary() * income_tax_rate
        social_security_tax = employee.get_salary() * social_security_tax_rate
        deductions.append((employee.get_full_name(), income_tax, social_security_tax))

    return deductions

employees = read_csv('machine_learning2024/final_task/employees.csv')

payroll_fund = calculate_payroll_fund(employees)
print(f"Фонд оплаты труда: {payroll_fund:.2f} рублей")

plot_salary_distribution(employees)

tax_deductions = calculate_tax_deductions(employees)
print("\nНалоговые отчисления:")
for deduction in tax_deductions:
    print(f"{deduction[0]}: Подоходный налог {deduction[1]:.2f} рублей, Соц. страхование {deduction[2]:.2f} рублей")

for employee in employees:
    employee.calculate_salary_indexation()
    programmer_bonus = employee.calculate_programmer_bonus()
    gender_bonus = employee.calculate_gender_bonus()
    print(f"{employee.get_full_name()} - Новая зарплата: {employee.get_salary():.2f} рублей, Премия программиста: {programmer_bonus:.2f} рублей, Праздничные выплаты: {gender_bonus} рублей")
