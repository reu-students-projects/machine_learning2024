def clean_and_split_text(text):
    cleaned_text = ''
    for char in text:
        if char.isalpha() or char.isspace():
            cleaned_text += char.lower()
    words = cleaned_text.split()
    return words

def count_word_frequency(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1  
        else:
            word_count[word] = 1  
    return word_count

def sort_word_frequency(word_count):
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words

def main():
    text = input("Введите текст: ")
    words = clean_and_split_text(text)
    word_count = count_word_frequency(words)
    sorted_word_frequency = sort_word_frequency(word_count)
    
    print("Частота слов в порядке убывания:")
    for word, count in sorted_word_frequency:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
