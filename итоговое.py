Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]# Данные, которые у нас есть
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

average_visits_per_day = sum(Week) / 7# 1. Рассчитываем среднее количество посещений в день

total_visits = sum(Week) # 2. Рассчитываем общее количество посещений за неделю

total_revenue = sum([Price[i] * Week[i] for i in range(len(Nail_style))]) # 3. Рассчитываем общую выручку салона за неделю

revenue_per_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))} # 4. Рассчитываем выручку по каждому виду маникюра


average_revenue_per_day_per_style = {style: revenue / 7 for style, revenue in revenue_per_style.items()}# 5. Рассчитываем среднюю выручку в день по видам маникюра


print(f"Среднее количество посещений в день: {average_visits_per_day:.2f}")# 6. Выводим результаты
print(f"Общее количество посещений за неделю: {total_visits}")
print(f"Общая выручка салона за неделю: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print(f"  {style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for style, average_revenue in average_revenue_per_day_per_style.items():
    print(f"  {style}: {average_revenue:.2f} руб.")

Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]# Данные, которые у нас есть
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

average_visits_per_day = sum(Week) / 7# 1. Рассчитываем среднее количество посещений в день

total_visits = sum(Week) # 2. Рассчитываем общее количество посещений за неделю

total_revenue = sum([Price[i] * Week[i] for i in range(len(Nail_style))]) # 3. Рассчитываем общую выручку салона за неделю

revenue_per_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))} # 4. Рассчитываем выручку по каждому виду маникюра


average_revenue_per_day_per_style = {style: revenue / 7 for style, revenue in revenue_per_style.items()}# 5. Рассчитываем среднюю выручку в день по видам маникюра


print(f"Среднее количество посещений в день: {average_visits_per_day:.2f}")# 6. Выводим результаты
print(f"Общее количество посещений за неделю: {total_visits}")
print(f"Общая выручка салона за неделю: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print(f"  {style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for style, average_revenue in average_revenue_per_day_per_style.items():
    print(f"  {style}: {average_revenue:.2f} руб.")



    # 1. Определяем функцию, которая принимает текст и анализирует частоту появления каждого слова
def analyze_text_frequency(text):
    # 2. Приводим текст к нижнему регистру и убираем знаки препинания с помощью регулярного выражения
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # 3. Разбиваем текст на слова, используя метод split(), который разбивает строку по пробелам
    words = cleaned_text.split()
    
    # 4. Используем Counter из модуля collections для подсчета частоты каждого слова
    word_count = Counter(words)
    
    # 5. Сортируем слова по частоте в порядке убывания, а если частота одинаковая — по алфавиту
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    # 6. Выводим каждое слово и его частоту
    for word, count in sorted_word_count:
        print(f'{word}: {count}')

# 7. Входной текст, который будем анализировать
text = """На шагающих утят быть похожими хотят,
Быть похожими хотят не зря, не зря.
Можно хвостик отряхнуть и пуститься в дальний путь
И пуститься в дальний путь, крича "кря-кря".
И природа хороша, и погода хороша,
Нет, не зря поет душа, не зря, не зря.
Даже толстый бегемот, неуклюжий бегемот
От утят не отстает, кряхтит "кря-кря"."""

# 8. Вызываем функцию с текстом
analyze_text_frequency(text)
