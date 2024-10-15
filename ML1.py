import string

def analyze_text(text):
    """
    Анализирует текст, подсчитывает количество вхождений каждого слова
    и возвращает словарь, где ключи - слова, значения - количество вхождений.
    """

    text = text.lower()  # Переводим текст в нижний регистр
    text = text.translate(str.maketrans('', '', string.punctuation))  # Удаляем пунктуацию
    words = text.split()  # Разбиваем текст на слова

    word_counts = {}  # Создаем словарь для подсчета слов
    for word in words:
        if word in word_counts:
            word_counts[word] += 1  # Если слово уже есть, увеличиваем счетчик
        else:
            word_counts[word] = 1  # Иначе добавляем слово в словарь со значением 1
            return word_counts  # Возвращаем словарь с подсчетом слов
# Получаем текст от пользователя
user_input = input("Введите текст: ")

# Анализируем текст
result = analyze_text(user_input)

# Выводим результаты
for word, count in result.items():
    print(f"{word}: {count}")
print("Выполнено")