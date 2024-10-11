# Колода карт Таро
tarot = {
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World",
    22: "The Fool"
}

# Извлекаем три карты: одну для прошлого, одну для настоящего и одну для будущего
past_card = tarot[1]   
present_card = tarot[2] 
future_card = tarot[3]  

print("Ваши карты:")
print(f"Прошлое: {past_card}")
print(f"Настоящее: {present_card}")
print(f"Будущее: {future_card}")
