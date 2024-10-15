Nail_style=['Shelak', 'French', 'Usial lak', 'Gel-lak', 'Akril']
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

def revenue (price, week):
    i = 0
    revenue = 0
    for price in Price:
        revenue += price * week[i]
        i += 1
    return revenue

def nail_style_revenues (style_, price_, week_):
    zipped_data = zip(style_, price_, week_)
    nail_style_revenues = {style: price * week for style, price, week in zipped_data}
    for style, revenue in nail_style_revenues.items():
        print(f'Average of {style} was {revenue}')

def avg_revenues (style_, price_, week_):
    zipped_data = zip(style_, price_, week_)
    avg_revenues = {style: round((price * week) / 7, ndigits=2) for style, price, week in zipped_data}
    for style, revenue in avg_revenues.items():
        print(f'The average revenue {style} was {revenue}')

total = sum(Week)

print('The average value of salon visits:', total / 5, '\n')
print('Total number of salon visits:', total, '\n')
print('Salon revenue', revenue(Price, Week), '\n')
print('Revenue by type of manicure:')
nail_style_revenues(Nail_style, Price, Week)
print('\nAverage revenue per day by type of manicure:')
avg_revenues(Nail_style, Price, Week)

                        

