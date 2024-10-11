from config import config
import requests


def get_coordinates(city: str, API_KEY: str):
    params = {
        'q': city,
        'limit': '1',
        'appid': API_KEY
    }
    response = requests.get(
        url=f'http://api.openweathermap.org/geo/1.0/direct',
        params=params
    )
    coordinates = None
    if (response.ok and len(response.json())):
        data = response.json()[0]
        coordinates = {
            "lat": data['lat'],
            "lon": data['lon'],
        }
    return coordinates


def kel_to_celsius(temp: float):
    return round(temp - 273.15)


def kph_to_mps(speed: float):
    return round(speed / 3.6)


def open_weather():
    API_KEY = config.OPEN_API_KEY
    city = input('Введите город: ')
    coordinates = get_coordinates(city, API_KEY)
    if coordinates:
        coordinates['lang'] = 'ru'
        coordinates['appid'] = API_KEY
        link = f"https://api.openweathermap.org/data/2.5/weather"
        response = requests.get(
            url=link,
            params=coordinates,
            timeout=2
        )
        if response.ok:
            data = response.json()
            print(
                f'''Погода в городе {data['name']}:
    Температура: {kel_to_celsius(data['main']['temp'])} °C
    Описание: {data['weather'][0]['description']}
    Ощущается как: {kel_to_celsius(data['main']['feels_like'])}
    Скорость ветра: {data['wind']['speed']} м/с
    Влажность: {data['main']['humidity']} %'''
            )
        else:
            print('Что-то пошло не так :(')
    else:
        print('По вашему запросу ничего не найдено :(')


def weather():
    url = 'http://api.weatherapi.com/v1/current.json'
    city = input('Введите город: ')

    params = {
        'key': config.WEATHER_API_KEY,
        'q': city,
        'lang': 'ru'
    }

    response = requests.get(
        url=url,
        params=params,
        timeout=2
    )
    if response.ok:
        data = response.json()
        reply_msg = f'''Погода в городе {data['location']['name']}:
    Температура: {data['current']['temp_c']} °C
    Описание: {data['current']['condition']['text']}
    Ощущается как: {data['current']['feelslike_c']} °C
    Скорость ветра: {kph_to_mps(data['current']['wind_kph'])} м/с
    Влажность: {data['current']['humidity']} %'''
        print(reply_msg)
    else:
        print(f'По вашеум запросу ничего не найдено')


try:
    input_status = False
    start_text = f'''Выберите сервис для получения погоды (1 или 2):
    1. Weather
    2. OpenWeather (менее стабилен)
Для выхода используйте ctrl+c'''
    print(start_text)

    while (not input_status):
        choose = input('Ваш выбор: ')
        if choose == '1':
            input_status = True
            weather()
        elif choose == '2':
            input_status = True
            open_weather()
        else:
            print(f"Проверьте введённые данные")

except KeyboardInterrupt:
    print(f'\nВыход из программы...')
except requests.exceptions.ReadTimeout:
    print(f"Ошибка получения данных с сервера")
