import requests

city = input("Город: ")
API_KEY = 'c93d447c029f99be158ff94c2aecf68a'
BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

def get_weather(city):
    try:
        response = requests.get(BASE_URL)

        if response.status_code == 404:
            print("Город не найден. Проверьте правильность ввода.")
        elif response.status_code != 200:
            print("Произошла ошибка при запросе данных.")

        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        print(f"Текущая погода в {city}:")
        print(f"Температура: {temp}°C")
        print(f"Описание: {description}")
        print(f"Влажность: {humidity}%")
    except requests.exceptions.RequestException as e:
        print("Ошибка подключение к API ",e)


get_weather(city)