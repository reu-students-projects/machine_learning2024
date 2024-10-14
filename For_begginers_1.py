import string

# Ввод текста от пользователя
text = input("Введите текст: ")

# Приводим текст к нижнему регистру и очищаем от знаков препинания
text = text.lower()
for char in string.punctuation:
    text = text.replace(char, "")

# Разбиваем текст на слова
words = text.split()

# Считаем частоту появления каждого слова
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Сортируем по частоте, а затем по алфавиту
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

# Выводим результат
for word, count in sorted_words:
    print(f"{word}: {count}")