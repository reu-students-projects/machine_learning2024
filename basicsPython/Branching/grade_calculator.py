# Вводим средний балл студента
grade = float(input("Введите средний балл студента: "))

# Определяем грейд на основе среднего балла
if grade >= 4.0:
    result = "A"
elif grade >= 3.0:
    result = "B"
elif grade >= 2.0:
    result = "C"
elif grade >= 1.0:
    result = "D"
elif grade >= 0.0:
    result = "F"
else:
    result = "Некорректный ввод"

print("Грейд студента:", result)
