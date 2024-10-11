import requests


def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric', 
        'lang': 'ru'  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        weather_data = response.json()

        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        print(f'Текущая погода в {city_name}:')
        print(f'Температура: {temperature}°C')
        print(f'Описание: {weather_description}')
        print(f'Влажность: {humidity}%')

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    except KeyError:
        print("Не удалось получить данные о погоде. Проверьте название города.")


if __name__ == "__main__":
    api_key = "2e701822db143ee888636fd324905449"  # Ключ API 
    cities = [  # Список городов для запроса погоды
        "Москва",
        "Санкт-Петербург",
        "Екатеринбург",
        "Новосибирск",
        "Казань",
        "Нижний Новгород",
        "Самара",
        "Челябинск",
        "Ростов-на-Дону",
        "Уфа"
    ]

    # Цикл для запроса погоды по каждому городу из списка
    for city in cities:
        print(f"\nЗапрашиваем погоду для города: {city}")
        get_weather(city, api_key)  