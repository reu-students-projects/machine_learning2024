# Данные
Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

# Расчет общего количества посещений
total_visits = sum(Week)

# Расчет средней посещаемости
average_visits = total_visits / len(Week)

# Расчет выручки по видам маникюра
revenue_per_style = [price * visits for price, visits in zip(Price, Week)]

# Общая выручка
total_revenue = sum(revenue_per_style)

# Средняя выручка в день по видам маникюра
average_revenue_per_day = [revenue / len(Week) for revenue in revenue_per_style]

print(f'Общее количество посещений салона: {total_visits}')
print(f'Среднее значение посещений салона: {average_visits:.2f}')
print(f'Общая выручка салона: {total_revenue} рублей')
print('Выручка по видам маникюра:')
for style, revenue in zip(Nail_style, revenue_per_style):
    print(f'{style}: {revenue} рублей')
print('Средняя выручка в день по видам маникюра:')
for style, average_revenue in zip(Nail_style, average_revenue_per_day):
    print(f'{style}: {average_revenue:.2f} рублей')
