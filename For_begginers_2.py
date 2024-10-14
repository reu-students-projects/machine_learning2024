# Данные
Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

# Среднее значение посещений салона
average_visits = sum(Week) / 7

# Общее количество посещений салона
total_visits = sum(Week)

# Выручка салона
revenue = sum(Price[i] * Week[i] for i in range(len(Nail_style)))

# Выручка по видам маникюра
revenue_by_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))}

# Средняя выручка в день по видам маникюра
average_daily_revenue_by_style = {Nail_style[i]: (Price[i] * Week[i]) / 7 for i in range(len(Nail_style))}

# Вывод результатов
print(f"Среднее значение посещений салона: {average_visits:.2f}")
print(f"Общее количество посещений салона: {total_visits}")
print(f"Общая выручка салона: {revenue} руб.")
print("\nВыручка по видам маникюра:")
for style, rev in revenue_by_style.items():
    print(f"{style}: {rev} руб.")

print("\nСредняя выручка в день по видам маникюра:")
for style, avg_rev in average_daily_revenue_by_style.items():
    print(f"{style}: {avg_rev:.2f} руб.")