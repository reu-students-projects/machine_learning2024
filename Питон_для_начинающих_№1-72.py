
# Задание 1
greetings = "Hello, world!"
print(greetings)

# Задание 2
length = 8 
width = 10 
area = length * width 
print("Площадь комнаты со сторонами", length, "и", width, ":" , area, " квадратных метров.") 
length_tiles = 20 
tiles_needed = length_tiles * width 
print("Количество плитки, необходимое для длины 20 плиток: ", tiles_needed, " квадратных метров.") 
new_length = 23 
new_width = 13 
new_area = new_length * new_width 
print("Площадь прямоугольника со сторонами", new_length, "и", new_width, ":" ,new_area, " квадратных метров.")

# Задание 3
print((6 * 6) - 1 == 8 + 1)
print(13 - 7 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1 )

print((6 * 6) - 1 >= 8 + 1)
print(13 - 7 <= (3 * 2) + 1)
print(3 * (2 - 1) > 4 - 1 )
      
# Задание 4
bool_variable_2 = True
print(type(bool_variable_2))

# Задание 5
user_name = input("Введите имя:")
dmitriy_check = "Дмитрий, твое рабочее мето находится в другой комнате. Отойди от чужого компьюетра и займись работой!"
others_check = "Добро пожаловать!"
if user_name == "Дмитрий":
    print(dmitriy_check)
else:
    print(others_check)

# Задание 6
statement_one = ((2 + 2 + 2 >= 6) and (-1 * -1 < 0))
statement_two = ((4 * 2 <= 8) and (7 - 1 == 6))
print(statement_one, statement_two)

# Задание 7
user_name = input("Введите имя: ")
apm = int(input("Введите номер рабочего места: "))
if (user_name == "Дмитрий" and apm == 1) or (user_name == "Ангелина" and apm == 2) or (user_name == "Василий" and apm == 3) or  (user_name == "Екатерина" and apm == 4):
    print("Добро пожаловать!")
if (user_name == "Ангелина" and apm != 2) or (user_name == "Василий" and apm != 3) or  (user_name == "Екатерина" and apm != 4): 
    print("Логин или пароль не верный, попробуйте еще раз.")
if user_name == "Дмитрий" and apm != 1:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
    
# Задание 8
statement_one = ((2 - 1 > 3) or (-5 * 2 == -10))
statement_two = ((9 + 5 <= 15) or (7 != 4 + 3))
print(statement_one, statement_two)

# Задание 9
user_name = input("Введите имя:")
apm = int(input("Введите номер рабочего места: "))
if (user_name == "Дмитрий" and apm == 1) or (user_name == "Ангелина" and apm == 2) or (user_name == "Василий" and apm == 3) or (user_name == "Екатерина" and apm == 4):
    print("Добро пожаловать!")
elif user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз.")
else:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

# Задание 10
grade = float(input("Введите средний балл студента: "))
if grade >= 4.0:
    print("Грейд: A")
elif grade >= 3.0:
    print("Грейд: B")
elif grade >= 2.0:
    print("Грейд: C")
elif grade >= 1.0:
    print("Грейд: D")
elif grade >= 0.0:
    print("Грейд: F")
else:
    print("Некорректный балл.")

# Задание 11
grade = float(input("Введите средний балл студента: "))
match grade:
    case grade if grade >= 4.0:
        result = "A"
    case grade if grade >= 3.0:
        result = "B"
    case grade if grade >= 2.0:
        result = "C"
    case grade if grade >= 1.0:
        result = "D"
    case grade if grade >= 0.0:
        result = "F"
    case _:
        result = "Некорректный балл."
print("Грейд студента:  ", (format(result)))

# Задание 12
def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием" + title + " with " + str(row_count) + "  lines")
create_spreadsheet("Загрузки")
create_spreadsheet("Приложения", 10)

# Задание 13
def define_age(current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = define_age(2049, 1993)
dads_age = define_age(2049, 1953)
print("Мне " + str(my_age) + " лет, а моему отцу " + str(dads_age) + " лет")

# Задание 14
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)
print("Нижний предел:", low_limit, ", верхний предел:", high_limit)

# Задание 15
def repeat_stuff(stuff, num_repeats = 10):
    return stuff * num_repeats
    
lyrics = repeat_stuff("Row", 3) + "Your Boat."
song = repeat_stuff("Row")
print(song)

# Задание 16
product_list = ["торт", 1]

# Задание 17
household_chemicals = [["стиральный порошок", 1],["средство для мытья посуды", 1]]

# Задание 18
names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

# Задание 19
orders = ['маргаритки', 'васильки']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)

# Задание 20
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

# Задание 21
list1 = range(9)
list2 = range(8)
print(list(list1), list(list2))

# Задание 22
ist1 = range(5,15,3)
list2 = range(0,40,5)
print(list(list1), list(list2))

# Задание 23
first_names = ['Анна', 'Борис', 'Александр', 'Денис']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range(0,4)
print(list(name_and_age), list(ids))

# Задание 24
list1 = range(2, 20, 2)
list1_len = len(list1)
print(list(list1))
print(list1_len)

list1 = range(2, 20, 3)
list1_len = len(list1)
print(list(list1))
print(list1_len)

# Задание 25
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print("Длина shopping_list:", len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print("Последний элемент:", last_element)
print("Элемент с индексом 5:", element5)

# Задание 26
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0:2]
print(beginning)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0:4]
print(beginning)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
middle = suitcase [2:4]
print(middle)

# Задание 27
suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase [:3]
print(start)

# Задание 28
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie',
'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

# Задание 29
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

# Задание 30
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

# Задание 31
inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двуспальная кровать', 'двуспальная кровать', 'комод', 'комод', 'стол', 'стол', 'тумбочка', 'тумбочка', 'королевский кровать', 'двуспальная кровать', 'две односпальные кровати', 'две односпальные кровати', 'простыни', 'простыни', 'подушка', 'подушка']
inventory_len = len(inventory)
print(inventory_len)
first = inventory[0]
print(first)
last = inventory[-1]
print(last)
inventory_2_6 = inventory[2:6]
print(inventory_2_6)
first_3 = inventory [:3]
print(first_3)
twin_beds = inventory.count("две односпальные кровати")*2
print(twin_beds)
inventory.sort()
print(inventory)

# Задание 32
order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
print(order)

# Задание 33
order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
order.insert(0, "закуска из овощей")
print(order)

# Задание 34
order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
order.insert(0, "закуска из овощей")
order.remove("салат капрезе")
print(order)

# Задание 35
order = ["паста", "пицца", "салат капрезе"]
order += ["цезарь", "кофе"]
order += ["красное сухое вино"]
order.insert(0, "закуска из овощей")
order.remove("салат капрезе")
order.pop(-1)
print(order)

# Задание 36
numbers = [0,1,2,3,4,5,6,7]
del numbers [3:5]
print(numbers)

# Задание 37
x = [15, 11, 13, 12, 14, 10]
x. reverse()
print(x)

# Задание 38
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
for game in sport_games:
    print(game)

# Задание 39
promise = "I will not chew gum in class"
for i in range(5):
 print("I will not chew gum in class")

# Задание 40
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    students_period_B.append(student)
    print(student)
print(students_period_B)

# Задание 41
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for breed in dog_breeds_available_for_adoption:
    print(breed) 
    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")  
        break
    
# Задание 42
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0 
for shop_sales in sales_data:
    for scoops in shop_sales:
        scoops_sold += scoops
print(scoops_sold)

# Задание 44
favour_word = "кошка"
print(favour_word)

# Задание 45
first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
print(new_account)
temp_password = last_name[2:6]
print(temp_password)

# Задание 46
def account_generator(first_name,last_name):
    first_name_3 = first_name[:3]
    last_name_3 = last_name[:3]
    new_account = first_name_3 + last_name_3
    print(new_account)
account_generator("Виталий","Красилов")
account_generator("Анна","Еремина")

# Задание 47
def password_generator(first_name, last_name):
    first_part = first_name[-3:]
    last_part = last_name[-3:]
    return first_part + last_part

temp_password = password_generator("Виталий","Красилов")
print(temp_password)

# Задание 48
company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)

# Задание 49
first_name = "Боб"  
fixed_first_name = "Р" + first_name[1:] 
print(fixed_first_name)

# Задание 50
print("theycallme\"crazy\"91")


# Задание 51
def get_length(text):
    count = 0
    for letter in text:
        count += 1 
    print(count)
get_length("Я люблю морковь")

# Задание 52
def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False
print(letter_check("Сережа","а"))


# Задание 53
def contains(big_string, little_string):
    return little_string in big_string

def common_letters(string_one, string_two):
    common = [] 
    for letter in string_one:
        if letter in string_two and letter not in common:  
            common.append(letter)  
    return common  
print(contains("watermelon", "melon"))  
print(contains("watermelon", "berry"))  
print(common_letters("banana", "cream"))

# Задание 54
def username_generator(first_name, last_name):
    if len(first_name) <= 3:
        user_first = first_name
    else:
        user_first = first_name[:3]
    if len(last_name) <= 4:
        user_last = last_name
    else:
        user_last = last_name[:4]
    username = user_first + user_last
    return username
print(username_generator("Abe", "Simpson"))

def password_generator(username):
    password = username[-1] + username[:-1]
    return password
print(password_generator(username_generator("Abe", "Simpson")))


# Задание 55
poem_title = "spring storm"
poem_author = "William Carlos Williams"
# Преобразуем заголовок стихотворения
poem_title_fixed = poem_title.title()
print("Исходный заголовок:", poem_title)
print("Отформатированный заголовок:", poem_title_fixed)

# Задание 56
line_one = "The sky has given over"
line_one_words = line_one.split()
print("Список слов:", line_one_words)

# Задание 57
authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
author_names = authors.split(", ")
author_last_names = [name.split()[-1] for name in author_names]
print("Список авторов:")
print(author_names)
print("\nСписок фамилий авторов:")
print(author_last_names)

# Задание 58
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
spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

# Задание 59
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["pantry"] = 22  
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}  # Добавлена запятая между "garage": 2 и "driveway": 1
print(sensors)
print(num_cameras)

# Задание 60
translations = {
    "mountain": "orod",
    "bread": "bass",
    "friend": "mellon",
    "horse": "roch"}
print(translations)

# Задание 61
animals_in_zoo = {}
animals_in_zoo["зебры"] = 8
animals_in_zoo["обезьяны"] = 12
animals_in_zoo["динозавры"] = 0
print(animals_in_zoo)

# Задание 62
ser_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
ser_ids.update ({"theLooper" : 138475, "stringQueen": 85739})
print(ser_ids)

# Задание 63
# Задание 63(1)
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
print(oscar_winners)
# Задание 63(2)
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

# Задание 64
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# Объединяем списки с помощью zip
zipped_drinks = zip(drinks, caffeine)
# Создаем словарь,
drinks_to_caffeine = {drink: mg_caffeine for drink, mg_caffeine in zipped_drinks}
print(drinks_to_caffeine)


# Задание 65
#Создание списков
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
# Создание словаря plays
plays = {song: playcount for song, playcount in zip(songs, playcounts)}
print("Словарь plays:")
print(plays)
#Добавление новой записи
plays["Purple Haze"] = 1
#Обновление количества воспроизведений для песни "Respect"
plays["Respect"] += 5
#Создание словаря library
library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}
print("\nСловарь library:")
print(library)

# Задание 66
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}
# Получаем знаки зодиака, связанные со стихией "земля"
earth_signs = zodiac_elements["earth"]
print("Знаки зодиака стихии 'земля':", earth_signs)

# Получаем знаки зодиака, связанные со стихией "огонь"
fire_signs = zodiac_elements["fire"]
print("Знаки зодиака стихии 'огонь':", fire_signs)


# Задание 67

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])  


# Задание 68
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
# Добавляем ключ "matcha" со значением 30
caffeine_level["matcha"] = 30
# Попытка вывести уровень кофеина в матче
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")

# Задание 69
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}
# Используем .get() для получения ID пользователя teraCoder
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)  
# Используем .get() для получения ID пользователя superStackSmash
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# Задание 70
user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10, 
    "syntax": 13, 
    "control flow": 15, 
    "loops": 22, 
    "lists": 19, 
    "classes": 18, 
    "dictionaries": 18
}
#Создание переменной users с объектом dict_keys для всех ключей user_ids
users = user_ids.keys()
#Создание переменной classes с объектом dict_keys для всех ключей num_exercises
classes = num_exercises.keys()
print(users)
print(classes)

# Задание 71
#Создаем переменную total_exercises и устанавливаем ее равной 0
total_exercises = 0
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

#Просматриваем значения в словаре и добавляем их к total_exercises
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)

# Задание 72
tarot = {
    1: "The Magician", 
    2: "The High Priestess", 
    3: "The Empress", 
    4: "The Emperor",
    5: "The Hierophant", 
    6: "The Lovers", 
    7: "The Chariot", 
    8: "Strength", 
    9: "The Hermit", 
    10: "Wheel of Fortune", 
    11: "Justice", 
    12: "The Hanged Man", 
    13: "Death", 
    14: "Temperance",
    15: "The Devil", 
    16: "The Tower", 
    17: "The Star", 
    18: "The Moon", 
    19: "The Sun", 
    20: "Judgement", 
    21: "The World", 
    22: "The Fool"
}
# Создаем пустой словарь для расклада
spread = {}
# Извлекаем карты и назначаем их значения
spread['прошлое'] = tarot[13]  
spread['настоящее'] = tarot[22] 
spread['будущее'] = tarot[10]  
print(spread)





















