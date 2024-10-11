# Словарь с идентификаторами пользователей
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# Получаем идентификатор пользователя teraCoder с значением по умолчанию 100000
tc_id = user_ids.get("teraCoder", 100000)
# Выводим tc_id в консоль
print(tc_id)

# Получаем идентификатор пользователя superStackSmash с значением по умолчанию 100000
stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)
