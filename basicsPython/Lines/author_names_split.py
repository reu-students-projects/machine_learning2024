# Длинная строка с именами авторов, разделенными запятыми
authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, " \
          "Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, " \
          "Langston Hughes, Adrienne Rich, Nikki Giovanni"

# Используем .split() для создания списка авторов
author_names = authors.split(", ")

print("Список авторов:")
print(author_names)

# Создаем список только с фамилиями авторов
author_last_names = [name.split()[-1] for name in author_names]

print("\nСписок фамилий авторов:")
print(author_last_names)
