import string
from collections import Counter

def analyze_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    word_count = Counter(words)
    sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

if __name__ == "__main__":
    user_input = input("Введите текст для анализа: ")
    analyze_text(user_input)
