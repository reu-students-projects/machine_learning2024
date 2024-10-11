from datetime import datetime
from typing import Optional
from string import capwords
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot
import csv, json, re, numpy

class Employee:
    def __init__(self, last_name: str, first_name: str, position: str, hire_date: datetime,
                 salary: int, sex: str, middle_name: Optional[str] = None):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__position = position
        self.__hire_date = hire_date
        self.__salary = salary
        self.__sex = sex
        self.__premium = 0
        self.__taxes = 0

    @staticmethod
    def write_to_json(employees, filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump([employee.to_dict() for employee in employees], file, ensure_ascii=False, indent=4)
            
    @staticmethod
    def write_to_csv(employees, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=employees[0].to_dict().keys(), delimiter=';')
            writer.writeheader()
            for employee in employees:
                writer.writerow(employee.to_dict())

    @staticmethod
    def parse_date(value: str) -> datetime:
        return datetime.strptime(value, '%d.%m.%Y')
    
    @staticmethod
    def wage_fund(employees: list) -> int:
        sum = 0
        for emp in employees:
            sum += emp.salary * 12 + round(0.03 * emp.salary if 'программист' in emp.position else 0) + 2000
        return sum
    
    @staticmethod
    def diagram(employees: list):
        filename = input("Введите имя файла (без расширения), в который хотите сохранить диаграмму: ")
        while not re.fullmatch(r'^(?!.*\.\.)(?!.*\.$)(?!^\.)(?!.*\/)(?!.*\\)[\w\-.]+$', 
                                filename):
            filename = input("Проверьте введое имя и повторите ввод: ")
        filepath = "diagrams/" + filename + ".png"
        positions = [emp.position.replace(" ", "\n") for emp in employees]
        pyplot.figure(figsize=(10, 6))
        pyplot.bar(positions, [emp.salary for emp in employees])
        pyplot.title("Размер оклада по должностям")
        pyplot.xlabel("Должности")
        pyplot.ylabel("Оклад")
        pyplot.savefig(filepath, dpi=300)
        while(1):
            choose = input("Открыть окно с диаграммой? (y/n) ")
            if choose == 'y': 
                pyplot.show()
                pyplot.close()
                break
            elif choose == 'n':
                pyplot.close()
                break
            else:
                print("Проверьте ввод")
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def middle_name(self) -> str:
        return self.__middle_name
    
    @property
    def position(self) -> str:
        return self.__position
    
    @property
    def hire_date(self) -> datetime:
        return self.__hire_date
    
    @property
    def salary(self) -> int:
        return self.__salary
    
    @property
    def sex(self) -> str:
        return self.__sex
    
    @property
    def premium(self) -> int:
        return self.__premium
    
    @property
    def full_name(self) -> str:
        return f'{self.__last_name} {self.__first_name}{(" " + self.__middle_name) if self.__middle_name else ""}'
    
    @property
    def print_everything(self) -> str:
        return f'''Сотрудник {self.full_name}: 
    Должность: {self.__position} 
    Дата найма: {self.__hire_date.strftime('%d.%m.%Y')}
    Оклад: {self.__salary}
    Пол: {self.__sex}
    Размер премии: {self.__premium if self.__premium else 0}'''
    
    @last_name.setter
    def last_name(self, value: str):
        if len(value) < 2:
            raise ValueError('Фамилия не может состоять из такого количества букв')
        if not re.fullmatch(r'^[А-Яа-яЁё]+$', value):
            raise ValueError('Фамилия должна быть написана кириллицей')
        self.__last_name = capwords(value)

    @first_name.setter
    def first_name(self, value: str):
        if len(value) < 2:
            raise ValueError('Имя не может состоять из такого количества букв')
        if not re.fullmatch(r'^[А-Яа-яЁё]+$', value):
            raise ValueError('Имя должно быть написано кириллицей')
        self.__first_name = capwords(value)

    @middle_name.setter
    def middle_name(self, value: str):
        if not value:
            self.__middle_name = None
        else:
            if len(value) < 3:
                raise ValueError('Отчество не может состоять из такого количества букв')
            if not re.fullmatch(r'^[А-Яа-яЁё]+$', value):
                raise ValueError('Отчество должно быть написано кириллицей')
            self.__middle_name = capwords(value)

    @position.setter
    def position(self, value: str):
        if len(value) < 2:
            raise ValueError('Название должности не может состоять из такого количества букв')
        self.__first_name = value

    @hire_date.setter
    def hire_date(self, value: str):
        date = self.parse_date(value)
        low_date = datetime(2000, 1, 1)
        if (date > datetime.now().strftime('%d.%m.%Y') or date < low_date):
            raise ValueError('Введена неверная дата')
        self.__hire_date = date

    @salary.setter
    def salary(self, value: int):
        if value < 0:
            raise ValueError('Зарплата не может быть отрицательной')
        self.__salary = value

    @sex.setter
    def sex(self, value: str):
        if capwords(value) != 'М' or capwords(value) != 'Ж':
            raise ValueError('Пол должен быть указан в формате М/Ж')
        self.__sex = value
    
    def prem_prog(self):
        if 'программист' in self.__position:
            self.__premium += self.__salary * 0.03
        
    def prem_wom(self) -> int:
        if self.__sex == 'Ж':
            self.__premium += 2000

    def prem_man(self) -> int:
        if self.__sex == 'М':
            self.__premium += 2000
    
    def index(self):
        if relativedelta(datetime.now(), self.__hire_date).years >= 10:
            self.__salary = round(self.__salary * 1.07)
        else:
            self.__salary = round(self.__salary * 1.05)
        
    def rest(self) -> bool:
        difference = relativedelta(datetime.now(), self.__hire_date)
        if difference.years > 0 or difference.months > 5:
            return True
        else:
            return False
    
    def to_dict(self) -> dict:
        return {
            "ФИО": self.full_name,
            "Должность": self.__position,
            "Дата найма": datetime.strftime(self.__hire_date, '%d.%m.%Y'),
            "Оклад": self.__salary,
            "Пол": self.__sex,
            "Размер премии": self.__premium
        }
    
    def taxes_counter(self) -> dict:
        sum_salary_prem = 0
        result = {}
        total_sum = 0
        for month in range(1, 13):
            month_prem = 0
            if (month == 2 and self.__sex == 'М') or (month == 3 and self.__sex == 'Ж'):
                month_prem += 2000
            if (month == 9 and 'программист' in self.__position):
                month_prem += self.__salary * 0.03
            if sum_salary_prem + self.__salary + month_prem <= 5000000:
                personal_inc_tax = round((self.__salary + month_prem) * 0.13, 2)
            elif sum_salary_prem <= 5000000:
                temp = 5000000 - sum_salary_prem
                personal_inc_tax = round(temp * 0.13 + (self.__salary + month_prem - temp) * 0.15, 2)
            else:
                personal_inc_tax = round(self.__salary * 0.15, 2)
            sum_salary_prem += self.__salary + month_prem
            month_sum = self.__salary + round((self.__salary + month_prem) * 0.3, 2)
            total_sum += month_sum
            result[month] = {
                'salary': self.__salary,
                'premium': month_prem,
                'taxes': {
                    'НДФЛ': personal_inc_tax,
                    'ФСС': round((self.__salary + month_prem) * 0.3, 2)
                },
                'month_sum': month_sum
            }
        result[13] = total_sum
        return result
    