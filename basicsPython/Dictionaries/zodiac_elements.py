# Словарь, который связывает стихии с их знаками зодиака
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Выводим список знаков зодиака, связанных со стихией «земля»
earth_signs = zodiac_elements["earth"]
print("Знаки зодиака стихии земля:", earth_signs)

# Выводим список знаков стихии огня
fire_signs = zodiac_elements["fire"]
print("Знаки зодиака стихии огня:", fire_signs)
