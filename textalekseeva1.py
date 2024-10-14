text = input('Введите текст: \n')
while True:
    line = input()
    if line == '':
        break
    text += ' ' + line

def replace_symbols(string: str, symbols_list: list[str] = [',', '"', '"', '!', '.', '\n'], replace_to: str = '') -> str:
    for symbol in symbols_list:
        string = string.replace(symbol, replace_to)
    return string

text = text.lower()
text = replace_symbols(text, symbols_list=['\n'], replace_to=' ')

text = text.split(' ')
unique_words = list(set(text))

dictionary = {}
for word in text:
    if word:
        dictionary[word] = dictionary.get(word, 0) + 1

def sorted_keys(item):
    return (-item[1], item[0])

sorted_words = sorted(dictionary.items(), key=sorted_keys)

print("Частота слов:")
for word, quantity in sorted_words:
    print(f"{word}: {quantity}")