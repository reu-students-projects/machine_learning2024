# Списки с названиями песен и количеством воспроизведений
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Создаем словарь с использованием генератора словаря и zip
plays = {song: playcount for song, playcount in zip(songs, playcounts)}

print(plays)
