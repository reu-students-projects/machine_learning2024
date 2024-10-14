#функция заменяет знаки препинания на пробелы
def replace_symbols (string:str, symbols_list:list[str]=['.', ',', '"', "!", ";", ":", "?", '*', '@', '%']) -> str:
    for symbol in symbols_list:
        string = string.replace(symbol, '')
    string = string.replace('\n', ' ')
    return string

def sorting (spisok:list):
    return spisok[1]

text = input('Введите текст: \n')
while True:
    line = input()
    if line == '':
        break
    text += ' ' + line

text = replace_symbols(text.lower())
text = text.split(' ')
unique_words = list(set(text))
unique_words.sort()

#slovar = {}
#for word in unique_words:
#    slovar[word] = text.count(word)
slovar = {word:text.count(word) for word in unique_words}

words = sorted(list(slovar.items()), reverse=True, key=sorting)
for pair in words:
    print(pair)