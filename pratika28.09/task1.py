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

def replace_symbols(string:str='', symbols_list:list[str]=['"','!','.',',',':'],replace_to:str='')->str:
    for symbol in symbols_list:
        string = string.replace(symbol, replace_to)
    return string

text = replace_symbols(text.lower())
text = replace_symbols(text, ['\n'], ' ')
text = text.split(' ')
unique_words = list(set(text))

result = {word: text.count(word) for word in unique_words}

# Сортировка по убыванию, при равенстве — по алфавиту
sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))

# Вывод результатов
for word, frequency in sorted_result:
    print(f'{word}: {frequency}')





