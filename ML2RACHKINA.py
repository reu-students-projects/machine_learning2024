from datetime import datetime
import csv
import json


class StaffMember:
    def init(self, surname, name, patronymic, job_title, start_date, salary_amount):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.job_title = job_title
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y")
        self.salary_amount = salary_amount

    def get_years_of_service(self):
        return (datetime.now() - self.start_date).days // 365

    def has_programmer_title(self):
        return 'программист' in self.job_title.lower()

    def is_woman(self):
        female_names = ['Анна', 'Екатерина', 'Алина', 'Светлана', 'Мария']
        return self.name in female_names

    def get_programmer_bonus(self):
        return self.salary_amount * 0.03 if self.has_programmer_title() else 0

    def get_march_bonus(self):
        return 2000 if self.is_woman() else 0

    def get_february_bonus(self):
        return 2000 if not self.is_woman() else 0

    def get_salary_adjustment(self):
        return self.salary_amount * (0.07 if self.get_years_of_service() > 10 else 0.05)

    def has_worked_over_half_year(self):
        return (datetime.now() - self.start_date).days > 183


staff_list = [
    StaffMember("Иванов", "Иван", "Иванович", "Менеджер", "22.10.2013", 250000),
    StaffMember("Сорокина", "Екатерина", "Матвеевна", "Аналитик", "12.03.2020", 75000),
    StaffMember("Струков", "Иван", "Сергеевич", "Старший программист", "23.04.2012", 150000),
    StaffMember("Корнеева", "Анна", "Игоревна", "Ведущий программист", "22.02.2015", 120000),
    StaffMember("Старчиков", "Сергей", "Анатольевич", "Младший программист", "12.11.2021", 50000),
    StaffMember("Бутенко", "Артем", "Андреевич", "Архитектор", "12.02.2010", 200000),
    StaffMember("Савченко", "Алина", "Сергеевна", "Старший аналитик", "13.04.2016", 100000)
]


def process_bonuses_and_adjustments(staff):
    for person in staff:
        prog_bonus = person.get_programmer_bonus()
        march_bonus = person.get_march_bonus()
        feb_bonus = person.get_february_bonus()
        salary_adj = person.get_salary_adjustment()

        print(f"{person.name} {person.surname}:")
        print(f"  Бонус программиста: {prog_bonus}")
        print(f"  Бонус к 8 марта: {march_bonus}")
        print(f"  Бонус к 23 февраля: {feb_bonus}")
        print(f"  Индексация зарплаты: {salary_adj}")


def filter_by_service_duration(staff, min_months=6):
    return [member for member in staff if (datetime.now() - member.start_date).days > min_months * 30]


def export_to_csv(staff, filename="staff.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия", "Имя", "Отчество", "Должность", "Дата начала", "Оклад"])
        for member in staff:
            writer.writerow([member.surname, member.name, member.patronymic, member.job_title,
                             member.start_date.strftime("%d.%m.%Y"), member.salary_amount])


def export_to_json(staff, filename="staff.json"):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump([member.dict for member in staff], file, ensure_ascii=False, indent=4)


process_bonuses_and_adjustments(staff_list)
long_term_staff = filter_by_service_duration(staff_list)
print("\nСотрудники, работающие более 6 месяцев:")

for member in long_term_staff:
    print(f"{member.name} {member.surname}")

export_to_csv(staff_list)
export_to_json(staff_list)
