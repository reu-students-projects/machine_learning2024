Nail_style = ['Шеллак', 'Френч', 'Обычный лак', 'Гель-лак', 'Акрил']
Price = [2000, 1500, 1000, 3000, 3500, 3200]
Week = [4, 5, 4, 8, 6]

#среднее значение посещений салона
print('Среднее значение посещений салона:', sum(Week)/len(Week))

#общее количество посещений салона
print('Общее количество посещений салона:', sum(Week))

#выручка салона
revenue = 0
for i in range(len(Week)):
    revenue += Price[i]*Week[i]
print('Выручка салона:', revenue)

# выручка по видам маникюра
print('Выручка по видам маникюра:')
styles_revenue = []
for i in range(len(Week)):
    styles_revenue.append(Price[i]*Week[i])
for i in range(len(Week)):
    print(Nail_style[i] + ' - ' + str(styles_revenue[i]))

# средняя выручка в день по видам маникюра
print('Средняя выручка в день по видам маникюра:')
avg_slyles_revenue = []
for i in range(len(Week)):
    avg_slyles_revenue.append(styles_revenue[i]/7)
for i in range(len(Week)):
    print(Nail_style[i] + ' - ' + str(avg_slyles_revenue[i]))