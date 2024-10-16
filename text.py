song_text = """
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
import string


def analyze_text(text):
    #убираем знаки препинания и приводим текст к нижнему регистру
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # разбиваем текст на слова
    words = text.split()

    # создаем словарь для хранения слов и их частоты
    frequency = {}

    # подсчитываем частоту каждого слова
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # преобразуем словарь в список для сортировки
    frequency_list = list(frequency.items())

    # сортируем по частоте (по убыванию) и по алфавиту
    frequency_list.sort(key=lambda x: (-x[1], x[0]))

    # выводим результаты
    print("частота слов:")
    for word, count in frequency_list:
        print("{}: {}".format(word, count))

def clean_text(text):
    # убираем знаки препинания и приводим текст к нижнему регистру
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return cleaned_text

#выводим исправленный текст
cleaned_song_text = clean_text(song_text)
print("исправленный текст:")
print(cleaned_song_text)

# анализируем текст песни
analyze_text(song_text)



