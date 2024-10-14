import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Для температуры в Цельсиях
        'lang': 'ru'  # Для русскоязычного описания погоды
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Вызывает ошибку для 4xx и 5xx
        weather_data = response.json()

        # Извлечение информации
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
    api_key = "2e701822db143ee888636fd324905449"
    city = input("Введите название города: ")
    get_weather(city, api_key)
