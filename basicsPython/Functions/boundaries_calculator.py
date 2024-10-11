# Определяем функцию get_boundaries
def get_boundaries(target, margin):
    low_limit = target - margin  # Вычисляем нижний предел
    high_limit = target + margin  # Вычисляем верхний предел
    return low_limit, high_limit  # Возвращаем пределы

# Вызываем функцию с параметрами target = 100 и margin = 20
low_limit, high_limit = get_boundaries(100, 20)

print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")
