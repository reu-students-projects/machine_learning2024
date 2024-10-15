text = '''На шагающих утят быть похожими хотят,
Быть похожими хотят
Не зря, не зря.
Можно хвостик отряхнуть и пуститься в дальний путь,
И пуститься в дальний путь, крича:
"Кря-кря!"
И природа хороша, и погода хороша,
Нет, не зря поет душа,
Не зря, не зря.
Даже толстый бегемот, неуклюжий бегемот
От утят не отстает, кряхтит:
"Кря-кря!"'''

text = text.lower()
def replace_symbols (string:str, symbols_list:list[str]=[',', '!', '.', '"'], replace_to='')->str:
    for symbols in symbols_list:
        string = string.replace(symbols, replace_to)
    return string

text = replace_symbols(text)
text = replace_symbols(text, ['\n'], ' ')
text = text.split(' ')

unique_list = list(set(text)) # оставляем только уникальные значения
result = {}
for word in unique_list:
    result[word] = text.count(word)
print(sorted(result.items(), key=lambda item: (-item[1], item[0])))