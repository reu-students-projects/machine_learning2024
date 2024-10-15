#===задание 1

text = '''На шагающих утят быть похожими хотят,
Быть похожими хотят
Не зря, не зря.
Можно хвостик отряхнуть и пуститься в дальний путь,
И пуститься в дальний путь, крича:
"Кря-кря!"
И природа хороша, и погода хороша,
Нет, не зря поет душа,
Не зря, не зря.
Даже толстый бегемот, неуклюжий бегемот
От утят не отстает, кряхтит:
"Кря-кря!"'''

text = text.lower()
def replace_symbols (string:str, symbols_list:list[str]=[',', '!', '.', '"'], replace_to='')->str:
    for symbols in symbols_list:
        string = string.replace(symbols, replace_to)
    return string

text = replace_symbols(text)
text = replace_symbols(text, ['\n'], ' ')
text = text.split(' ')

unique_list = list(set(text)) # оставляем только уникальные значения
result = {}
for word in unique_list:
    result[word] = text.count(word)
print(sorted(result.items(), key=lambda item: (-item[1], item[0])))





#===задание 2

Nail_style=['Шеллак', 'Френч', 'Обычный лак', 'Гель-лак', 'Акрил']
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

def revenue (price, week):
    i = 0
    revenue = 0
    for price in Price:
        revenue += price * week[i]
        i += 1
    return revenue

def nail_style_revenues (style_, price_, week_):
    zipped_data = zip(style_, price_, week_)
    nail_style_revenues = {style: price * week for style, price, week in zipped_data}
    for style, revenue in nail_style_revenues.items():
        print(f'Выручка за {style} составила {revenue}')

def avg_revenues (style_, price_, week_):
    zipped_data = zip(style_, price_, week_)
    avg_revenues = {style: round((price * week) / 7, ndigits=2) for style, price, week in zipped_data}
    for style, revenue in avg_revenues.items():
        print(f'Средняя выручка за {style} составила {revenue}')

total = sum(Week)

print('Среднее значение посещений салона:', total / 5, '\n')
print('Общее количество посещений салона:', total, '\n')
print('Выручка салона', revenue(Price, Week), '\n')
print('Выручка по видам маникюра:')
nail_style_revenues(Nail_style, Price, Week)
print('\nСредняя выручка в день по видам маникюра:')
avg_revenues(Nail_style, Price, Week)