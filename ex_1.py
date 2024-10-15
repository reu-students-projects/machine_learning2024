def replace(string: str, list1: list[str] = [',', '!', ':', ';', '"', '\'', '.', '-', '?'], replace_to: str = '') -> str:
    for symbol in list1:
        string = string.replace(symbol, replace_to)
    return string

text = input("Введите текст: ").lower()

text = replace(text)

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(f"{word}: {count}")