# Данные
Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

# Расчет
total_visits = sum(Week)  # Общее количество посещений
average_visits = total_visits / 7  # Среднее значение посещений в день
total_revenue = sum(price * visits for price, visits in zip(Price, Week))  # Общая выручка

# Выручка по видам маникюра
revenue_per_style = {style: price * visits for style, price, visits in zip(Nail_style, Price, Week)}

# Средняя выручка в день по видам маникюра
average_revenue_per_style = {style: revenue / 7 for style, revenue in revenue_per_style.items()}

# Вывод
print(f"Среднее значение посещений салона в день: {average_visits:.2f}")
print(f"Общее количество посещений салона: {total_visits}")
print(f"Выручка салона: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print(f"{style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for style, avg_revenue in average_revenue_per_style.items():
    print(f"{style}: {avg_revenue:.2f} руб.")
