Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]
DAYS_IN_WEEK = 7
# 1. cоздание словаря для удобства доступа к данным
salon_data = {}
for style, price, count in zip(Nail_style, Price, Week):
    salon_data[style] = {
        "price": price,
        "count": count
    }

# 2. вычисление общего количества посещений
total_visits = sum(Week)

# 3. вычисление среднего значения посещений в день
average_visits_per_day = total_visits / DAYS_IN_WEEK

# 4. вычисление общей выручки салона
total_revenue = sum(salon_data[style]["price"] * salon_data[style]["count"] for style in Nail_style)

# 5. вычисление выручки по видам маникюра
revenue_per_style = {}
for style in Nail_style:
    revenue = salon_data[style]["price"] * salon_data[style]["count"]
    revenue_per_style[style] = revenue

# 6. вычисление средней выручки в день по видам маникюра
average_daily_revenue_per_style = {}
for style in Nail_style:
    average_daily_revenue = revenue_per_style[style] / DAYS_IN_WEEK
    average_daily_revenue_per_style[style] = average_daily_revenue


# выручка салона
print("Общая выручка салона за неделю: {} рублей".format(total_revenue))

# выручка по видам маникюра
print("\nВыручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print("{}: {} рублей".format(style, revenue))

# средняя выручка в день по видам маникюра
print("\nСредняя выручка в день по видам маникюра:")
for style, avg_revenue in average_daily_revenue_per_style.items():
    print("{}: {:.2f} рублей".format(style, avg_revenue))


