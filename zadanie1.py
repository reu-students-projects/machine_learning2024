text = input("Введите текст: ")

# Преобразуем текст в нижний регистр и убираем знаки препинания
text = text.lower()
for ch in ",.!?;:":
    text = text.replace(ch, '')

# Разбиваем текст на слова
words = text.split()

# Считаем количество каждого слова
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Сортируем слова по частоте и выводим их
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

# Выводим результат
for word, count in sorted_words:
    print(word, count)
