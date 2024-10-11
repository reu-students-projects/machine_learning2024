# Список доступных пород собак для усыновления
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

# Итерация по списку пород собак
for breed in dog_breeds_available_for_adoption:
    print(breed)  # Печать текущей породы
    if breed == dog_breed_I_want:  # Проверка на совпадение с желаемой породой
        print("У них есть собака, которую я хочу!")
        break  # Прерывание цикла при нахождении желаемой породы
