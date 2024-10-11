text = '''На шагающих утят быть похожими хотят,
Быть похожими хотят
Не зря, не зря.
Можно хвостик отряхнуть и пуститься в дальний путь,
И пуститься в дальний путь, крича:
"Кря-кря"
И природа хороша, и погода хороша,
Нет, не зря поет душа,
Не зря, не зря.
Даже толстый бегемот, неуклюжий бегемот
От утят не отстает, кряхтит:
"Кря-кря!"'''

# замена символов 
def replace_symbols(string: str = '', symbols_list: list[str] = ['"', '!', '.', ',', ':'], replace_to: str = '') -> str:
    for symbol in symbols_list:  # Проходим по каждому символу из списка
        string = string.replace(symbol, replace_to)  # Заменяем символ на заданный
    return string

# Приводим текст к нижнему регистру и убираем лишние символы
text = replace_symbols(text.lower())

# Заменяем символ переноса строки на пробел
text = replace_symbols(text, ['\n'], ' ')

# Разбиваем строку на слова по пробелу
text = text.split(' ')

# Извлекаем уникальные слова 
unique_words = list(set(text))

# Подсчитываем количество каждого уникального слова
result = {word: text.count(word) for word in unique_words}

# Сортировка по убыванию частоты слов, при одинаковой частоте — по алфавиту
sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))

# результат: слово и его частота
for word, frequency in sorted_result:
    print(f'{word}: {frequency}')




