# Определяем функцию, которая принимает строку и возвращает её длину
def get_length(input_string):
    length = 0
    # Перебираем каждый символ в строке, чтобы подсчитать количество символов
    for char in input_string:
        length += 1
    return length

test_string = "Привет, мир!"
length_of_string = get_length(test_string)

print("Длина строки:", length_of_string)
