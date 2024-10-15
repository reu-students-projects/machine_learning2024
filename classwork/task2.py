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