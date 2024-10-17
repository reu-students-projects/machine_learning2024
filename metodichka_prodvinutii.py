import csv
import datetime
import json
import os
import matplotlib.pyplot as plt
class Employee:
    def __init__(self, fullname: str, position: str, start_date: str, salary: int):
        self.fullname = fullname
        self.position = position
        self.start_date = start_date
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not value:
            raise ValueError("Имя не может быть пустым")
        self.__salary = value

    # перевод элемента класса в словарь
    def to_dict(self):
        return vars(self)

    # рассчет премии программистам
    def calculate_bonus(self):
        return int(int(self.__salary) * 0.03) if 'программист' in self.position.lower() else 0

    # премия в 2к в марте и феврале
    def feb_march_bonus(self):
        return 2000

    # индексаци ЗП в зависимости от времени работы в компании
    def experience_index(self):
        start_list = [int(i) for i in self.start_date.split('.')]
        start = datetime.date(start_list[-1], start_list[-2], start_list[-3])
        work_experience = datetime.date.today() - start
        return int(self.__salary) * 1.07 if work_experience.days > 3650 else int(self.__salary) * 1.05

    # дает добро на отпуск, если проработал в компании больше 6 лет (в задании 6 месяцев)
    def is_vacation_ready(self):
        start_list = [int(i) for i in self.start_date.split('.')]
        start = datetime.date(start_list[-1], start_list[-2], start_list[-3])
        work_experience = datetime.date.today() - start
        return True if work_experience.days > 2190 else False


# функция записи в сsv
def write_csv(filename: str, fields: list, data: list):
    write_header = os.path.exists(filename)
    with open(filename, 'w', newline='') as output_csv:
        output_writer = csv.writer(output_csv, delimiter=';')
        if write_header:
            output_writer.writerow(fields)
        for row in data:
            output_writer.writerow(row.values())


# функция записи в json
def write_json(filename: str, data: list):
    with open(filename, 'w') as output_json:
        for row in data:
            json_writer = json.dumps(row, ensure_ascii=False, indent=4)
            output_json.write(json_writer + '\n')

# фонд оплаты труда
def salary_fond(emp_list: list):
    sum = 0
    for element in emp_list:
        sum += int(element['_Employee__salary']) + int(element['Премия программистам']) + int(element['Премия на праздники'])
    return sum

# построение диаграммы
def bar_chart(category: list, values: list):
    plt.bar(category, values)
    plt.title('Оклад по должностям')
    plt.show()


with open('emp_data.csv', newline='') as emp_data:
    emp_reader = csv.DictReader(emp_data, delimiter=';')
    csv_fields = ['ФИО', 'Должность', 'Дата найма', 'Оклад c индексацией', 'Премия программистам',
                  'Премия на праздники',
                  'Пора ли в отпуск']
    csv_list = []
    for row in emp_reader:
        person = Employee(fullname=row['ФИО'], position=row['Должность'], start_date=row['Дата найма'], salary=row['Оклад'])
        person.salary = person.experience_index()
        output_dict = person.to_dict()
        output_dict.update({'Премия программистам': person.calculate_bonus(),  'Премия на праздники': person.feb_march_bonus(),
                            'Пора ли в отпуск': person.is_vacation_ready()})
        csv_list.append(output_dict)

write_csv('output.csv', csv_fields, csv_list)
write_json('output.json', csv_list)
print(f'Фонд оплаты труда: {salary_fond(csv_list)} рублей')
cat_lst = [el['position'] for el in csv_list]
val_lst = [int(el['_Employee__salary']) for el in csv_list]
bar_chart(cat_lst, val_lst)



