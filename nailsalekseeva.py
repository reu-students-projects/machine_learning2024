
nail_styles = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
prices = [2000, 1500, 1000, 3000, 3500]
weekly_visits = [4, 5, 4, 8, 6]


total_visits = sum(weekly_visits)  
average_daily_visits = total_visits / 7  
total_revenue = sum(price * visits for price, visits in zip(prices, weekly_visits)) 

revenue_per_style = {style: price * visits for style, price, visits in zip(nail_styles, prices, weekly_visits)}

average_daily_revenue_per_style = {style: revenue / 7 for style, revenue in revenue_per_style.items()}

print(f"Среднее значение посещений салона в день: {average_daily_visits:.2f}")
print(f"Общее количество посещений салона: {total_visits}")
print(f"Выручка салона: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print(f"{style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for style, avg_revenue in average_daily_revenue_per_style.items():
    print(f"{style}: {avg_revenue:.2f} руб.")