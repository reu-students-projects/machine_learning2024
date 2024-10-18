text = '''На шагающих утят быть похожими хотят,
Быть похожими хотят не зря, не зря.
Можно хвостик отряхнуть и пуститься в дальний путь
И пуститься в дальний путь, крича "кря-кря".
И природа хороша, и погода хороша,
Нет, не зря поет душа, не зря, не зря.
Даже толстый бегемот, неуклюжий бегемот
От утят не отстает, кряхтит "кря-кря"'''
text = text.lower()
text = text.replace(',', '').replace('.', '').replace('"', '').replace('"', '')
text = text.split()

unique = list(text)

result ={word:text.count(word) for word in set(text)}

def get_freq(item):
    return (-item[1]), item[0]
def  sort_freq(item):
    return item[0]

sorted_result = dict(sorted(result.items(), key=get_freq))

print(sorted_result)