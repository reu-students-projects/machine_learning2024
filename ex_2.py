Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

average_visits = sum(Week) / len(Week)
print(f"Среднее количество посещений салона за неделю: {average_visits}")

total_visits = sum(Week)
print(f"Общее количество посещений салона за неделю: {total_visits}")

total_revenue = sum(Price[i] * Week[i] for i in range(len(Nail_style)))
print(f"Общая выручка салона за неделю: {total_revenue} рублей")


print("Выручка по видам маникюра:")
for i in range(len(Nail_style)):
    revenue = Price[i] * Week[i]
    print(f"{Nail_style[i]}: {revenue} рублей")

days_in_week = 7
print("Средняя выручка в день по видам маникюра:")
for i in range(len(Nail_style)):
    daily_revenue = (Price[i] * Week[i]) / days_in_week
    print(f"{Nail_style[i]}: {daily_revenue:.2f} рублей в день")