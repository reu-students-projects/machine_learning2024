# Определяем функцию, которая проверяет, содержит ли большая строка меньшую
def contains(big_string, little_string):
    return little_string in big_string

# Определяем функцию, которая возвращает список уникальных общих букв двух строк
def common_letters(string_one, string_two):
    # Создаем множество для хранения уникальных букв
    common_chars = set()

    # Ищем общие буквы в обеих строках
    for char in string_one:
        if char in string_two:
            common_chars.add(char)

    # Преобразуем множество в список и возвращаем его
    return list(common_chars)

result_contains = contains("watermelon", "melon")
result_common_letters = common_letters("banana", "cream")

print(f"Содержит ли 'watermelon' 'melon'? {result_contains}")
print(f"Общие буквы между 'banana' и 'cream': {result_common_letters}")
