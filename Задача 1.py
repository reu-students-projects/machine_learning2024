# Программу, которая принимает текст от пользователя и анализирует частоту появления каждого слова в этом тексте.

import string  

def analyze_text(text):
    text = text.lower()  
    text = text.translate(str.maketrans("", "", string.punctuation))  
 
    words = text.split()  
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1  
        else:
            word_freq[word] = 1  
    
    sorted_words = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))
    
    for word, freq in sorted_words:
        print(f'{word}: {freq}')
user_text = input("Введите текст: ")
analyze_text(user_text)
