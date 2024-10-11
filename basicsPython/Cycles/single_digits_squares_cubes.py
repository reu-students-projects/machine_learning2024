# Создание списка single_digits с числами от 0 до 9 (включительно)
single_digits = list(range(10))

# Цикл for для вывода каждого элемента single_digits
for digit in single_digits:
    print(digit)

# Создание пустого списка squares
squares = []

# Цикл для добавления квадратов элементов single_digits в squares
for digit in single_digits:
    squares.append(digit ** 2)  # Добавление квадрата элемента

# Вывод списка squares
print(squares)

# Создание списка cubes, где каждый элемент возводится в куб
cubes = [digit ** 3 for digit in single_digits]

print(cubes)
