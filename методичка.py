#Необходимо расчитать, сколько плитки понадобится для проведения ремонта в 
#комнате! Создать переменные length и width и присвоить в них значения 8 и 10 
#соответственно.
length = 8  
width = 10 
tile_length = 0.5  # длина плитки в метрах
tile_width = 0.5   # ширина плитки в метрах
room_area = length * width # Вычисление площади комнаты
tile_area = tile_length * tile_width # Вычисление площади одной плитки
number_of_tiles = room_area / tile_area # Расчет количества плиток
print(f"Количество плитки, необходимое для ремонта: {number_of_tiles:.0f}")

#Оказалось, что произошла ошибка в расчетах и в длину необходимо 20 плиток.
#Какое количество плитки понадобится в этом случае?
# Данные комнаты
length_tiles = 20 
tile_length = 0.5  
width = 10          
length = length_tiles * tile_length # Вычисление длины комнаты в метрах
room_area = length * width # Вычисление площади комнаты
tile_area = tile_length * tile_length # Вычисление площади одной плитки
number_of_tiles = room_area / tile_area # Расчет количества плиток
print(f"Количество плитки, необходимое для ремонта: {number_of_tiles:.0f}")
#Рассчитать площадь прямоугольника со сторонами 23, 13
length = 23  # длина прямоугольника
width = 13   # ширина прямоугольника
area = length * width  # вычисляем площадь, умножая длину на ширину
print(f"Площадь прямоугольника: {area}")  # выводим результат
#Создайте переменную с именем bool_variable и установите для нее значение true.
#Попробуйте вывести ее в консоль. Какая ошибка у вас вывелась? Почему?
bool_variable = true  # ошибка: 'true' не определен
print(bool_variable)  # попытка вывести значение
NameError: name 'true' is not defined

#В Python правильное написание булевого значения — это True с заглавной буквы.
#Замените значение в bool_variable на ‘true’ (в кавычках) Проверьте тип


#Функция type(bool_variable) возвращает <class 'str'>, что подтверждает, что переменная теперь имеет тип строка.
#Создайте переменную с именем bool_variable_2 и сделайте так, чтобы она имелв
#логический тип истины.
bool_variable_2 = True  # присваиваем логическое значение
print(bool_variable_2)  # выводим значение
# Проверяем тип переменной
print(type(bool_variable_2))  # выводим тип

#Проверить истинность следующих выражений:
(2+2+2 >=6) and  (-1 * -1 < 0)
(4*2 <= 8) and (7 -1 == 6)
(4 * 2 <= 8) and (7 - 1 == 6)
#Результат проверки поместить в переменные statement_one и statement_two.
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0) # Проверяем первое выражение
statement_two = (4 * 2 <= 8) and (7 - 1 == 6) # Проверяем второе выражение
# Выводим результаты
print(statement_one)  # выводит: False
print(statement_two)  # выводит: False

#Я работаю в компании, обслуживающей проблемы информационной безопасности
#на других предприятиях. К нам обратился директор маленькой рекламной компании.
#Основная проблема в том, что у них есть охранник Дмитрий, который устанавливает
#компьютерные игры на АРМ (автоматизированные рабочие места) сотрудников, когда тех
#нет на работе по долгу (находятся в отпуске) и играет всеми ночами напролет. Поэтому
#вас просят разработать приложение, которое проверяло введенные учетные и
#разграничивало права сотрудников. Для охранника Дмитрия просят сделать
#специализированное уведомление: «Дмитрий, твое рабочее место находится в другой
#комнате. Отойди от чужого компьютера и займись работой!».

# 1. Вводим переменную user_name
user_name = input("Введите ваше имя: ")
# 2. Текст для Дмитрия
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
# 3. Сообщение для других сотрудников
welcome_message = "Добро пожаловать!"
# 4. Оператор if для проверки имени пользователя
if user_name == "Дмитрий":
    print(Dmitriy_check)  # выводим сообщение для Дмитрия
else:
    print(welcome_message)  # выводим общее сообщение для остальных сотрудников

#Наша компания продолжает разрабатывать приложение по безопасности для
#рекламной компании. Теперь, если пользователь 3 раза ввел пароль неправильно,
#необходимо заблокировать систему. Для этого выполним следующие действия:
# 1. Вводим переменную, фиксирующую количество попыток ввода
enter_number = int(input("Введите количество попыток ввода пароля: "))

# 2. Оператор if для проверки количества попыток
if enter_number < 3:
    remaining_attempts = 3 - enter_number
    print(f"Попробуйте еще раз. У вас осталось {remaining_attempts} попыток.")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")


# Вводим переменные для имени пользователя и номера АРМ
user_name = input("Введите ваше имя: ")
ARM = int(input("Введите номер вашего АРМ (1-4): "))

# Проверяем соответствие имени пользователя и номера АРМ
if (user_name == "Дмитрий" and ARM == 1) or \
   (user_name == "Ангелина" and ARM == 2) or \
   (user_name == "Василий" and ARM == 3) or \
   (user_name == "Екатерина" and ARM == 4):
    print("Добро пожаловать!")
elif user_name != "Дмитрий" and ARM != 1:
    print("Логин или пароль не верный, попробуйте еще раз.")
elif user_name == "Дмитрий" and ARM != 1:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
 
# Вводим переменные для имени пользователя и номера АРМ
user_name = input("Введите ваше имя: ")
ARM = int(input("Введите номер вашего АРМ (1-4): "))

# Проверяем соответствие имени пользователя и номера АРМ
if user_name == "Дмитрий":
    if ARM == 1:
        print("Добро пожаловать!")
    else:
        print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
elif user_name == "Ангелина" and ARM == 2:
    print("Добро пожаловать!")
elif user_name == "Василий" and ARM == 3:
    print("Добро пожаловать!")
elif user_name == "Екатерина" and ARM == 4:
    print("Добро пожаловать!")
else:
    print("Логин или пароль не верный, попробуйте еще раз.")


# Вводим переменную для среднего балла
grade = float(input("Введите ваш средний балл (0-4): "))

# Проверяем значение среднего балла и присваиваем соответствующий грейд
if grade >= 4.0:
    print("Ваш грейд: A")
elif grade >= 3.0:
    print("Ваш грейд: B")
elif grade >= 2.0:
    print("Ваш грейд: C")
elif grade >= 1.0:
    print("Ваш грейд: D")
elif grade >= 0.0:
    print("Ваш грейд: F")
else:
    print("Неверный балл. Пожалуйста, введите значение от 0 до 4.")



# Вводим переменную для среднего балла
grade = float(input("Введите ваш средний балл (0-4): "))

# Используем match/case для определения грейда
match grade:
    case _ if grade >= 4.0:
        print("Ваш грейд: A")
    case _ if grade >= 3.0:
        print("Ваш грейд: B")
    case _ if grade >= 2.0:
        print("Ваш грейд: C")
    case _ if grade >= 1.0:
        print("Ваш грейд: D")
    case _ if grade >= 0.0:
        print("Ваш грейд: F")
    case _:
        print("Неверный балл. Пожалуйста, введите значение от 0 до 4.")


def create_spreadsheet(title, row_count=1000):
    # Выводим строку с информацией о создании электронной таблицы
    print("Создание электронной таблицы с названием " + title + " с " + str(row_count) + " строками")

# Вызов функции с заголовком «Загрузки»
create_spreadsheet("Загрузки")


# Вызов функции для вычисления возраста
my_age = calc_age(2049, 1993)  # Сохраняем результат в my_age
dads_age = calc_age(2049, 1953)  # Сохраняем результат в dads_age

# Выводим результаты на консоль
print(f"Мне {my_age} лет, а моему отцу {dads_age} лет.")


def get_boundaries(target, margin):
    # Вычисляем нижний и верхний предел
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit  # Возвращаем значения в указанном порядке

# Вызов функции с параметрами target=100 и margin=20
low_limit, high_limit = get_boundaries(100, 20)

# Выводим результаты на консоль
print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")


def repeat_stuff(stuff, num_repeats=10):
    # Возвращаем повторяемую строку
    return stuff * num_repeats

# Вызов функции с использованием "Row" и 3
lyrics = repeat_stuff("Row", 3) + " Your Boat."

# Создаем переменную song с вызовом repeat_stuff только с stuff
song = repeat_stuff("Row")

# Выводим песню в консоль
print(song)


Names=[‘Ben’, ‘Holly’, ‘Ann’]
dogs_names= [‘Sharik’, ‘Gab’, ‘Beethoven’]

names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

# Создание zip-объекта
names_and_dogs_names = zip(names, dogs_names)

# Преобразуем zip-объект в список для отображения
names_and_dogs_names_list = list(names_and_dogs_names)

# Вывод результата
print(names_and_dogs_names_list)
2 Создайте новую переменную с именем list_of_names_and_dogs_names, вызвав
list () для names_and_dogs_names. Выведите в консоль новую переменную.
names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

# Создание zip-объекта
names_and_dogs_names = zip(names, dogs_names)

# Преобразуем zip-объект в список
list_of_names_and_dogs_names = list(names_and_dogs_names)

# Вывод новой переменной
print(list_of_names_and_dogs_names)


orders = ['маргаритки', 'васильки'].

# Создание списка заказов
orders = ['маргаритки', 'васильки']

# Вывод заказов
print("Заказы, которые он получил сегодня:", orders)


# Создание списка заказов
orders = ['маргаритки', 'васильки']

# Новый заказ на тюльпаны
orders.append('тюльпаны')

# Новый заказ на розы
orders.append('розы')

# Вывод всех заказов
print("Заказы, которые получила сегодня Мария:", orders)


orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
# broken_prices = [5, 3, 4, 5, 4] + 4
# Существующий список заказов
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

# Новые заказы
new_orders = orders + ['сирень', 'ирис']

# Вывод нового списка заказов
print("Обновленный список заказов:", new_orders)
Удалите # перед списком broken_prices. Если вы запустите этот код, вы
получите сообщение об ошибке
# Существующий список заказов
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

# Новый список с ценами
broken_prices = [5, 3, 4, 5, 4] + 4
Исправьте команду, чтобы она выполнялась без ошибок.
# Существующий список заказов
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

# Новый список с ценами (правильный способ)
broken_prices = [5, 3, 4, 5, 4] + [4]  # Добавляем 4 как элемент списка

# Вывод списка цен
print("Цены:", broken_prices)


list1=[1,8]

my_list = list(range(0, 9))

#Создайте диапазон с именем list2 с числами от 0 до 7
list2 = list(range(0, 8))

#Измените функцию диапазона, создавшую list1, так, чтобы она:
#• Начиналась с 5
#• Разница между каждым элементом составляет 3 единицы.
#• Заканчивается на 15
list1 = диапазон (6, 15, 2)
list1 = list(range(5, 15, 3))

#Создайте объект диапазона с именем list2, который:
#• Начинается с 0
#• Разница между каждым элементом составляет 5 единиц.
#• Заканчивается до 40
list2 = list(range(0, 40, 5))


# 1. Создаем список имен клиентов
first_names = ["Анна", "Борис", "Александр", "Денис"]
# 2. Создаем пустой список для возрастов
age = []
# 3. Добавляем возраст Дениса в список age
age.append(42)
# 4. Создаем список возрастов для всех клиентов и добавляем возраст Дениса
all_ages = [32, 41, 29]  # Возраст Анны, Бориса и Александра
all_ages.append(age[0])  # Добавляем возраст Дениса
# 5. Объединяем списки first_names и all_ages с помощью zip
name_and_age = list(zip(first_names, all_ages))
# 6. Создаем диапазон с идентификационными номерами для каждого клиента
ids = list(range(0, 4))
# Выводим результаты для проверки
print("Список имен:", first_names)
print("Список возрастов:", all_ages)
print("Имена и возрасты:", name_and_age)
print("Идентификационные номера:", ids)

list1 = range (2, 20, 2)

# 1. Создаем диапазон list1
list1 = range(2, 20, 2)

# Вычисляем длину list1 и сохраняем в переменной list1_len
list1_len = len(list(list1))

# 2. Используем print для проверки list1_len
print("Длина list1:", list1_len)

# 1. Создаем новый диапазон list1, пропуская 3 элемента
list1 = range(2, 20, 3)
# Вычисляем длину list1 и сохраняем в переменной list1_len
list1_len = len(list(list1))
# 2. Используем print для проверки list1_len
print("Длина list1:", list1_len)

#Используйте print и len, чтобы отобразить длину shopping_list.
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
# Создаем список покупок
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']

# Используем print и len для отображения длины shopping_list
print("Длина shopping_list:", len(shopping_list))


# Создаем список покупок
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']

# 2. Получаем последний элемент и сохраняем в переменной last_element
last_element = shopping_list[-1]

# 3. Получаем элемент с индексом 5 и сохраняем в переменной element5
element5 = shopping_list[5]

# 4. Используем print для отображения element5 и last_element
print("Элемент с индексом 5:", element5)
print("Последний элемент:", last_element)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0: 2]

# Создаем список чемодана
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']

# Получаем первые два элемента и сохраняем в переменной beginning
beginning = suitcase[0:2]

# Используем print для проверки переменной beginning
print("beginning:", beginning)

# Считываем количество элементов в списке suitcase
list_length = len(suitcase)
print("Количество элементов в suitcase:", list_length)

# Создаем список чемодана
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
# 2. Изменяем beginning, чтобы оно выделяло первые 4 элемента
beginning = suitcase[0:4]
print("beginning:", beginning)
# 3. Создаем новый список middle, содержащий два средних элемента из чемодана
middle = suitcase[2:4]  # два средних элемента: 'брюки' и 'брюки'
print("middle:", middle)

suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
# Создаем список чемодана
suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
# Создаем новый список start, содержащий первые 3 элемента
start = suitcase[0:3]
# Выводим список start на экран
print("start:", start)

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie',
'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

# Список голосов
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 
         'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 
         'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
# Используем метод count для подсчета голосов за Jake
jake_votes = votes.count('Jake')
# Выводим количество голосов за Jake на экран
print("Количество голосов за Jake:", jake_votes)

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace'
, '1600 Pennsylvania Ave', '10 Downing St.']

# Исходный список адресов
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', 
             '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Выводим адреса до сортировки
print("Адреса до сортировки:", addresses)

# Сортируем список адресов
addresses.sort()

# Выводим адреса после сортировки
print("Адреса после сортировки:", addresses)


games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

# Исходный список игр
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

# Создаем новый отсортированный список
games_sorted = sorted(games)

# Выводим исходный и отсортированный списки
print("Игры до сортировки:", games)
print("Игры после сортировки:", games_sorted)


# Исходный список инвентаря
inventory = [
    'двухспальная кровать', 'двухспальная кровать', 'изголовье',
    'двуспальная кровать', 'двуспальная кровать', 'комод',
    'комод', 'стол', 'стол', 'тумбочка', 'тумбочка',
    'королевский кровать', 'двуспальная кровать', 'две односпальные кровати',
    'две односпальные кровати', 'простыни', 'простыни', 'подушка', 'подушка'
]

# 1. Количество товаров на складе
inventory_len = len(inventory)

# 2. Первый элемент
first = inventory[0]

# 3. Последний элемент
last = inventory[-1]

# 4. Элементы с индекса 2 до индекса 6 (не включая)
inventory_2_6 = inventory[2:6]

# 5. Первые 3 предмета
first_3 = inventory[:3]

# 6. Количество односпальных кроватей
twin_beds = inventory.count('две односпальные кровати')

# 7. Сортировка инвентаря
inventory.sort()

# Вывод результатов
print("Количество товаров на складе:", inventory_len)
print("Первый элемент:", first)
print("Последний элемент:", last)
print("Элементы с индекса 2 до 6:", inventory_2_6)
print("Первые 3 предмета:", first_3)
print("Количество односпальных кроватей:", twin_beds)
print("Инвентарь после сортировки:", inventory)

# 1. Создаем список заказов
order = ['паста', 'пицца', 'салат капрезе']

# 2. Добавляем заказ от нового посетителя
order.append('салат цезарь')
order.append('кофе')

# 3. Добавляем красное сухое вино в заказ
order.append('красное сухое вино')

# Выводим итоговый список заказа
print("Заказ:", order)

# Исходный список заказов
order = ['паста', 'пицца', 'салат капрезе', 'салат цезарь', 'кофе', 'красное сухое вино']

# 1. Добавляем закуску из овощей в начало списка
order.insert(0, 'закуска из овощей')

# Выводим обновленный список заказа
print("Обновленный заказ:", order)

# Исходный список заказов
order = ['закуска из овощей', 'паста', 'пицца', 'салат капрезе', 'салат цезарь', 'кофе', 'красное сухое вино']

# 1. Удаляем салат капрезе из списка
order.remove('салат капрезе')

# Выводим обновленный список заказа
print("Обновленный заказ после удаления:", order)

# Исходный список заказов
order = ['закуска из овощей', 'паста', 'пицца', 'салат цезарь', 'кофе', 'красное сухое вино']

# 1. Удаляем красное сухое вино из списка
order.remove('красное сухое вино')

# Выводим обновленный список заказа
print("Обновленный заказ после удаления:", order)

# 1. Создаем список чисел от 0 до 7
numbers = list(range(8))  # [0, 1, 2, 3, 4, 5, 6, 7]

# 2. Удаляем 2 элемента из середины списка
# В данном случае середина - это 3 и 4 (индексы 3 и 4)
del numbers[3:5]  # Удаляем элементы с индексами 3 и 4

# Выводим обновленный список
print("Обновленный список чисел:", numbers)

x = [15, 11, 13, 12, 14, 10]
# Исходный список
x = [15, 11, 13, 12, 14, 10]
# Меняем порядок элементов на месте
x.reverse()
print("Список в обратном порядке:", x)

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
print(game)

IndentationError.


# Исходные списки
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

# Цикл для вывода настольных игр
for game in board_games:
    print(game)  # Добавлен отступ

# Цикл для вывода видов спорта
for sport in sport_games:
    print(sport)

promise = "I will not chew gum in class"
# Обещание
promise = "I will not chew gum in class"

# Цикл for для печати обещания 5 раз
for i in range(5):
    print(promise)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
2 Внутри цикла for, после добавления student к student_period_B, выведите student.
# Списки студентов
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

# Цикл for для добавления студентов
for student in students_period_A:
    students_period_B.append(student)  # Добавляем студента в student_period_B
    print(student)  # Выводим имя студента после добавления

# Проверка результата
print("Объединённый список студентов:", students_period_B)

# Список доступных пород собак
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

# Цикл for для итерации по списку пород собак
for breed in dog_breeds_available_for_adoption:
    print(breed)  # Печатаем текущую породу
    # Проверяем, совпадает ли порода с желаемой
    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")  # Сообщение, если порода совпадает
        break  # Завершение цикла, если совпадение найдено

# Данные о продажах
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# Инициализация переменной для хранения общего количества проданных мороженых
scoops_sold = 0

# Цикл по списку sales_data
for store_sales in sales_data:
    # Цикл по каждому числу в вложенном списке
    for scoops in store_sales:
        scoops_sold += scoops  # Добавляем количество к общему количеству

# Выводим общее количество проданных мороженых
print("Общее количество проданных мороженых:", scoops_sold)

# 1. Создаем список single_digits с числами от 0 до 9
single_digits = list(range(10))

# 2. Цикл for, который выводит каждое число из single_digits
for digit in single_digits:
    print(digit)  # Выводим текущее число

# 3. Создаем список squares и инициализируем его пустым списком
squares = []

# 4. Внутри цикла добавляем квадрат каждого элемента single_digits в squares
for digit in single_digits:
    squares.append(digit ** 2)  # Добавляем квадрат числа
    # Вывод элемента можно сделать здесь, если нужно
    # print(digit)  

# 5. Выводим squares
print("Квадраты чисел:", squares)

# 6. Создаем список cubes, возводя каждый элемент single_digits в куб
cubes = [digit ** 3 for digit in single_digits]

# 7. Выводим cubes
print("Кубы чисел:", cubes)

# 1. Сохраняем слово "бронетранспортёр" в переменной favour_word
favour_word = "бронетранспортёр"

# 2. Выводим favour_word
print(favour_word)

# 1. Записываем имя и фамилию сотрудника
first_name = "Виталий"
last_name = "Красилов"

# 2. Создаем переменную new_account, беря первые пять букв last_name
new_account = last_name[:5]  # Срезаем первые пять букв фамилии

# Выводим результат
print("Имя:", first_name)
print("Фамилия:", last_name)
print("Учётная запись:", new_account)

# Фамилия сотрудника
last_name = "Красилов"

# Создаем переменную temp_password, беря срез с третьей по шестую буквы last_name
temp_password = last_name[2:6]  # Индексы 2, 3, 4, 5 (третья по шестую)

# Выводим результат
print("Временный пароль:", temp_password)

def account_generator(first_name, last_name):
    # Объединяем первые три буквы имени и фамилии
    account_name = first_name[:3] + last_name[:3]
    return account_name

# Проверяем функцию с именем и фамилией сотрудника
first_name = "Виталий"
last_name = "Красилов"

# Сохраняем результат в переменную new_account
new_account = account_generator(first_name, last_name)

# Выводим результат
print("Имя учетной записи:", new_account)

def password_generator(first_name, last_name):
    # Объединяем последние три буквы имени и фамилии
    password = first_name[-3:] + last_name[-3:]
    return password

# Проверяем функцию с именем и фамилией сотрудника
first_name = "Виталий"
last_name = "Красилов"

# Сохраняем результат в переменную temp_password
temp_password = password_generator(first_name, last_name)

# Выводим результат
print("Временный пароль:", temp_password)


# Находим предпоследний символ
second_to_last = company_motto[-2]

# Создаем фрагмент из последних 4 символов
final_word = company_motto[-4:]

# Выводим результаты
print("Предпоследний символ:", second_to_last)
print("Последние 4 символа:", final_word)

first_name = "Обычное имя"  # Например, пример неправильного имени

# Объединяем "Р" с фрагментом first_name, который включает все, кроме первого символа
fixed_first_name = "Р" + first_name[1:]

# Выводим результат
print("Исправленное имя:", fixed_first_name)

#1.	Когда Роб Дейли настраивал свою учетную запись, он установил свой пароль:
#theycallme"crazy"91
#Его пароль вызывал некоторые ошибки в системе из-за отметок ". Перепишите его пароль, используя escape-символы, и сохраните его с переменным паролем.
password = "theycallme\"crazy\"91"#\

# Выводим результат
print("Пароль:", password)


def get_length(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count

# Пример использования функции
test_string = "Пример строки"
length_of_string = get_length(test_string)

# Выводим результат
print("Длина строки:", length_of_string)


def letter_check(word, letter):
    return letter in word

# Пример использования функции
test_word = "пример"
test_letter = "и"

result = letter_check(test_word, test_letter)

# Выводим результат
print("Содержит ли слово букву?", result)

def contains(big_string, little_string):
    return little_string in big_string

# Пример использования функции
result1 = contains("watermelon", "melon")
result2 = contains("watermelon", "berry")

print("Содержит ли 'watermelon' 'melon'?", result1)  # True
print("Содержит ли 'watermelon' 'berry'?", result2)  # False

def common_letters(string_one, string_two):
    # Создаём множества уникальных букв из обеих строк
    set_one = set(string_one)
    set_two = set(string_two)
    
    # Находим пересечение множеств
    common = set_one.intersection(set_two)
    
    # Возвращаем список из найденных общих букв
    return list(common)

# Пример использования функции
result_common = common_letters("banana", "cream")
print("Общие буквы:", result_common)  # ['a']
#1.	Руководство компании снова заручилось вашей помощью, чтобы создать функцию для создания имени пользователя и пароля. В этом упражнении вы создадите две функции: username_generator и password_generator.

def username_generator(first_name, last_name):
    # Получаем первые 3 буквы имени
    if len(first_name) < 3:
        username_first_part = first_name
    else:
        username_first_part = first_name[:3]

    # Получаем первые 4 буквы фамилии
    if len(last_name) < 4:
        username_second_part = last_name
    else:
        username_second_part = last_name[:4]
        
    # Формируем имя пользователя
    username = username_first_part + username_second_part
    return username

def password_generator(username):
    # Если имя пользователя пустое, возвращаем пустую строку
    if not username:
        return ""
    
    password = ""
    
    # Используем цикл for для перебора символов в имени пользователя
    for i in range(len(username)):
        if i == len(username) - 1:
            # Если это последний символ, добавляем его в начало пароля
            password = username[i] + password
        else:
            # Добавляем текущий символ в конец пароля
            password += username[i]
    
    # Возвращаем или сдвинутый список символов обратно в строку
    return password

# Пример использования
first_name = "Abe"
last_name = "Simpson"
username = username_generator(first_name, last_name)
password = password_generator(username)

print(f"Имя пользователя: {username}")
print(f"Временный пароль: {password}")

# Исходные данные
poem_title = "spring storm"
poem_author = "William Carlos Williams"

# Преобразование заголовка стиха
poem_title_fixed = poem_title.title()

# Выводим оригинальный и отформатированный заголовок
print(f"Исходный заголовок: {poem_title}")
print(f"Отформатированный заголовок: {poem_title_fixed}")


# Исходная строка
line_one = "The sky has given over"

# Создаем список слов, разделяя строку по пробелам
line_one_words = line_one.split()

# Выводим полученный список слов
print(line_one_words)

authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
# Исходная строка с именами авторов
authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

# Создаем список авторов, разделяя строку по запятым
author_names = authors.split(", ")

# Выводим полученный список имен авторов
print(author_names)

# Исходная строка с именами авторов
authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

# Создаем список авторов, разбивая строку по запятым
author_names = authors.split(", ")

# Создаем список фамилий авторов
author_last_names = [name.split()[-1] for name in author_names]

# Выводим полученный список фамилий авторов
print(author_last_names)

#1.	Организация прислала вам полный текст стихотворения Уильяма Карлоса Уильямса «Весенняя буря». Они хотят, чтобы вы разбили стихотворение на отдельные строки.
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

# Полный текст стихотворения
spring_storm_text = """The sky has given over  
its bitterness.  
Out of the dark change  
all day long  
rain falls and falls  
as if it would never end.  
Still the snow keeps  
its hold on the ground.  
But water, water  
from a thousand runnels!  
It collects swiftly,  
dappled with black  
cuts a way for itself  
through green ice in the gutters.  
Drop after drop it falls  
from the withered grass-stems  
of the overhanging embankment."""

# Создаем список строк, разбивая текст по строкам
spring_storm_lines = spring_storm_text.splitlines()

# Выводим полученный список строк
print(spring_storm_lines)

1.	Предположим, у нас есть словарь датчиков температуры в доме и текущие значения температуры. Мы только что добавили датчик в «кладовую», он показывает 22 градуса.
Добавьте эту пару в словарь:
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}

# Исходный словарь датчиков температуры
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

# Добавляем новый датчик в "кладовую"
sensors["pantry"] = 22

# Выводим обновленный словарь
print(sensors)

2.	Скопируйте строчку кода ниже и удалите символ # перед определением словаря num_cameras, который представляет количество камер в каждой области вокруг дома.
Если вы запустите этот код, вы получите сообщение об ошибке:
SyntaxError: invalid syntax
Попробуйте найти и исправить синтаксическую ошибку, чтобы запустить этот код.
#num_cameras = {"backyard": 6,  "garage": 2 "driveway" 1}

num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Выводим словарь для проверки
print(num_cameras)

1.	Создайте словарь переводов, который сопоставляет следующие слова на английском языке с их определениями на синдарине (языке эльфов):
English	Sindarin
mountain	orod
bread	bass
friend	mellon
horse	roch

# Создаем словарь переводов
translations = {
    "mountain": "orod",
    "bread": "bass",
    "friend": "mellon",
    "horse": "roch"
}

# Выводим словарь для проверки
print(translations)

#1. Создаем пустой словарь
animals_in_zoo = {}

# 2. Добавляем зебр
animals_in_zoo["зебры"] = 8

# 3. Добавляем обезьян
animals_in_zoo["обезьяны"] = 12

# 4. Добавляем динозавров
animals_in_zoo["динозавры"] = 0

# 5. Выводим словарь в консоль
print(animals_in_zoo)


# Исходный словарь user_ids
user_ids = {
    "teraCoder": 9018293,
    "proProgrammer": 119238
}

# 1. Добавляем новых пользователей
user_ids["theLooper"] = 138475
user_ids["stringQueen"] = 85739

# 2. Выводим словарь в консоль
print(user_ids)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# Данные списки
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# 1. Создаем итеративный объект с парами напитков и кофеина
zipped_drinks = zip(drinks, caffeine)

# 2. Создаем словарь drinks_to_caffeine с использованием генерации словаря
drinks_to_caffeine = {drink: caffeine_content for drink, caffeine_content in zipped_drinks}

# Выводим результирующий словарь в консоль
print(drinks_to_caffeine)


# Данные списки
songs = [
    "Like a Rolling Stone",
    "Satisfaction",
    "Imagine",
    "What's Going On",
    "Respect",
    "Good Vibrations"
]
playcounts = [78, 29, 44, 21, 89, 5]

# 1. Создаем словарь plays
plays = {song: count for song, count in zip(songs, playcounts)}

# 2. Выводим plays
print("Initial plays:", plays)

# 3. Добавляем новую запись для "Purple Haze"
plays["Purple Haze"] = 1

# 4. Увеличиваем количество воспроизведений для "Respect" на 5
plays["Respect"] += 5

# 5. Создаем словарь library
library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}

# 6. Выводим library
print("Library:", library)



# Данные словаря
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# 1. Выводим список знаков зодиака, связанных со стихией «земля»
earth_signs = zodiac_elements["earth"]
print("Знаки зодиака элемента 'земля':", earth_signs)

# 2. Выводим список знаков стихии огня
fire_signs = zodiac_elements["fire"]
print("Знаки зодиака элемента 'огонь':", fire_signs)


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius
"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# Данные словаря
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Попробуем получить доступ к несуществующему ключу "energy"
try:
    energy_signs = zodiac_elements["energy"]
except KeyError as e:
    print(f"KeyError: {e}")
# Добавляем ключ "energy"
zodiac_elements["energy"] = "Not a Zodiac element"

# Теперь пытаемся получить доступ к "energy" снова
energy_signs = zodiac_elements["energy"]
print("Energy:", energy_signs)



# Данные словаря
caffeine_level = {
    "espresso": 64,
    "chai": 40,
    "decaf": 0,
    "drip": 120
}

# Добавляем ключ "matcha" со значением 30
caffeine_level["matcha"] = 30

# Используем блок try/except для попытки вывести уровень кофеина в матче
try:
    matcha_caffeine = caffeine_level["matcha"]
    print("Уровень кофеина в матче:", matcha_caffeine)
except KeyError:
    print("Неизвестный уровень кофеина")


# Данные словаря
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# 1. Получаем значение идентификатора пользователя teraCoder
tc_id = user_ids.get("teraCoder", 100000)
print("tc_id:", tc_id)

# 2. Получаем значение идентификатора пользователя superStackSmash
stack_id = user_ids.get("superStackSmash", 100000)
print("stack_id:", stack_id)
