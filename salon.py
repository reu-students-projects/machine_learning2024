Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

total_visits = sum(Week)
average_visits = total_visits / len(Week)
total_revenue = sum([Price[i] * Week[i] for i in range(len(Price))])
revenue_by_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))}
average_daily_revenue = {Nail_style[i]: (Price[i] * Week[i]) / 7 for i in range(len(Nail_style))}

print(f"Среднее значение посещений: {average_visits:.2f}")
print(f"Общее количество посещений: {total_visits}")
print(f"Выручка салона: {total_revenue}")
print("Выручка по видам маникюра:")
for style, revenue in revenue_by_style.items():
    print(f"{style}: {revenue}")
print("Средняя выручка в день по видам маникюра:")
for style, avg_revenue in average_daily_revenue.items():
    print(f"{style}: {avg_revenue:.2f}")