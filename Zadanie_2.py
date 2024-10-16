Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

total_visits = sum(Week)
print(f"Общее количество посещений салона: {total_visits}")

average_visits = total_visits / len(Week)
print(f"Среднее значение посещений салона: {average_visits:.2f}")

total_revenue = sum(price * visits for price, visits in zip(Price, Week))
print(f"Выручка салона: {total_revenue} рублей")

revenue_per_style = {style: price * visits for style, price, visits in zip(Nail_style, Price, Week)}
print("Выручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print(f"{style}: {revenue} рублей")

average_daily_revenue_per_style = {style: revenue / 7 for style, revenue in revenue_per_style.items()}
print("Средняя выручка в день по видам маникюра:")
for style, average_revenue in average_daily_revenue_per_style.items():
    print(f"{style}: {average_revenue:.2f} рублей")

