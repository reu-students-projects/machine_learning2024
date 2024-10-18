Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500, 3200]
Week = [4, 5, 4, 8, 6]


# среднее значение посещение салона
srednee = sum (Week)/len(Week)
print (srednee)

# общее кол-во посещения салона
summa = sum(Week)
print(summa)

#выручка салона
revenue = sum(Price)
print (revenue)

# Выручка по видам маникюра
revenue= []
for i in range(len(Nail_style)):
    total_revenue = Price[i] * Week [i]
    revenue.append(total_revenue)
    print (f'Тип маникюра:{Nail_style [i]}, Цена: {Price[i]} руб., Кол-во: {Week[i]}, Выручка:{revenue[i]} руб.')

#Средняя выручка в день по видам маникюра
revenue_srednee= []
for i in range(len(Nail_style)):
    total_revenue_day =  total_revenue = Price[i] * Week [i]
    revenue_srednee.append(total_revenue_day/Week[i])
    print (f'Тип маникюра: {Nail_style [i]}, Cредняя выручка в день: {revenue_srednee[i]}')