names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

# Используем zip для объединения имен и имен собак
names_and_dogs_names = zip(names, dogs_names)

# Преобразуем zip-объект в список
list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)
