import requests

weather_key = '2004279af20cb5608542f54c9fb00a95'
url = 'http://api.openweathermap.org/data/2.5/weather'
city = input('Введите город на английском: ')
data = {'q': city, 'APPID': weather_key, 'units': 'metric'}
response = requests.get(url, params=data)

if response.status_code != 404:
    response = response.json()['main']
    temperature = round(response["temp"])
    pressure = round(response["pressure"] / 10 * 7.50063, 2)
    humidity = response["humidity"]
    print(
        f"Погода в г. {city.capitalize()}\n"
        f"температура: {temperature} C\n"
        f"атмосферное давление: {pressure} мм.рт.ст\n"
        f"влажность: {humidity} %"
    )
else:
    print(" такой город точно есть? перепроверь, я такого не знаю ")
