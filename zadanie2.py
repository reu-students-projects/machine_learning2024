Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500] 
Week = [4, 5, 4, 8, 6]

total_visits = sum(Week)
average_visits = total_visits / len(Week)
revenue_by_style = [price * count for price, count in zip(Price, Week)]
total_revenue = sum(revenue_by_style)
average_daily_revenue_by_style = [revenue / 7 for revenue in revenue_by_style]

print(f"Общее количество посещений салона: {total_visits}")
print(f"Среднее значение посещений салона: {average_visits:.2f}")
print(f"Общая выручка салона: {total_revenue} рублей")
for style, revenue in zip(Nail_style, revenue_by_style):
    print(f"Выручка по виду '{style}': {revenue} рублей")
for style, average_daily_revenue in zip(Nail_style, average_daily_revenue_by_style):
    print(f"Средняя выручка в день по виду '{style}': {average_daily_revenue:.2f} рублей")
