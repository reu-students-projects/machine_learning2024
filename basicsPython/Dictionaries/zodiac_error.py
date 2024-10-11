 # Словарь, который связывает стихии с их знаками зодиака
zodiac_signs = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Попробуем получить доступ к элементу 'energy', который не существует
try:
    print(zodiac_signs["energy"])
except KeyError as e:
    print(f"KeyError: {e} - ключ 'energy' не существует.")

# Добавляем ключ 'energy' со значением 'Not a Zodiac element'
zodiac_signs["energy"] = "Not a Zodiac element"

# Проверяем, устранен ли KeyError
try:
    print(zodiac_signs["energy"])
except KeyError as e:
    print(f"KeyError: {e} - ключ 'energy' не существует.")
