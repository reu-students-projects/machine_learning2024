# Определяем функцию, которая проверяет наличие буквы в слове
def letter_check(word, letter):
    # Проверяем, содержится ли буква в слове
    if letter in word:
        return True
    else:
        return False

test_word = "Программирование"
test_letter = "г"
result = letter_check(test_word, test_letter)

print(f"Слово '{test_word}' содержит букву '{test_letter}': {result}")
