#Некоторая статистика по одной неделе в компании.

Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

total_visits = sum(Week)

average_visits = total_visits / len(Week)

# 3. Общая выручка
total_revenue = sum([Price[i] * Week[i] for i in range(len(Nail_style))])

# 4. Выручка по видам маникюра
revenue_by_nail_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))}

# 5. Средняя выручка в день по видам маникюра (предположим, что неделя состоит из 7 дней)
average_revenue_per_day = {Nail_style[i]: revenue_by_nail_style[Nail_style[i]] / 7 for i in range(len(Nail_style))}

print(f"Среднее количество посещений за неделю: {average_visits:.2f}")
print(f"Общее количество посещений за неделю: {total_visits}")
print(f"Общая выручка за неделю: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for nail_style, revenue in revenue_by_nail_style.items():
    print(f"  {nail_style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for nail_style, avg_daily_revenue in average_revenue_per_day.items():
    print(f"  {nail_style}: {avg_daily_revenue:.2f} руб. в день")
