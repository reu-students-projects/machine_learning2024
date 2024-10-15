import requests

def get_weather(city_name):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=89cec0395f1fe074ac4b459c6b8016d1&units=metric&lang=ru"
        weather_data = requests.get(url).json()
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        
        print(f"Текущая погода в {city}:")
        print(f"Температура: {temperature}°C")
        print(f"Описание: {description}")
        print(f"Влажность: {humidity}%")
        return {
            "city": city,
            "temperature": temperature,
            "description": description,
            "humidity": humidity
        }

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Ошибка подключения: {err}")
    except KeyError:
        print("Ошибка: Неверное название города или отсутствуют данные.")
        
def main():
    cities = ['Москва', 'Лондон', 'Нью-Йорк', 'Париж', 'Токио', 'Берлин', 'Пекин', 'Рим', 'Сидней', 'Дубай']
    weather_dataset = []

    for city in cities:
        print(f"Получение погоды для: {city}")
        weather_info = get_weather(city)
        print("~"*30)
        if weather_info:
            weather_dataset.append(weather_info)

    print("\nНабор данных о погоде в разных городах:")
    for data in weather_dataset:
        print(data)

if __name__ == "__main__":
    main()
