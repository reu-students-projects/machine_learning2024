# Вводим средний балл студента
grade = float(input("Введите средний балл студента: "))

# Определяем грейд на основе среднего балла с использованием match/case
match grade:
    case g if g >= 4.0:
        result = "A"
    case g if g >= 3.0:
        result = "B"
    case g if g >= 2.0:
        result = "C"
    case g if g >= 1.0:
        result = "D"
    case g if g >= 0.0:
        result = "F"
    case _:
        result = "Некорректный ввод"

# Выводим соответствующий грейд
print("Грейд студента:", result)
