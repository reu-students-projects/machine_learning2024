test_text = """
На танцующих утят быть похожими хотят,
Быть похожими хотят
Не зря, не зря.
Повторяйте все за мной, все фигуры до одной,
Все фигуры до одной,
Кря-кря-кря-кря.
Легче танца в мире нет, лучше танца в мире нет,
Вам раскрыт его секрет
Не зря, не зря.
Посмотрите, бегемот, неуклюжий бегемот,
Вот танцует, вот дает!
Кря-кря-кря-кря!
"""

def word_frequency_analysis(text):
    import string
    text = text.lower()
    text = text.replace("-", " ")
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print(f"{word}: {count}")

word_frequency_analysis(test_text)