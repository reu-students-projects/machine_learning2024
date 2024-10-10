import requests
import json
def get_weather(city):
    api_key ="0bfda06c596baa6adda9ffbcdcf0b167"  
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = json.loads(response.text)
        city_name = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        return city_name, temperature, description, humidity
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных о погоде: {e}")
        return None, None, None, None
    except (KeyError, IndexError):
        print("Не удалось получить необходимые данные о погоде.")
        return None, None, None, None
    except json.JSONDecodeError:
        print("Ошибка при обработке ответа API.")
        return None, None, None, None

city = input("Введите название города: ")
city_name, temperature, description, humidity = get_weather(city)
if city_name is not None:
        print(f"Текущая погода в {city_name}:")
        print(f"Температура: {temperature}°C")
        print(f"Описание: {description}")
        print(f"Влажность: {humidity}%")
else:
        print("Не удалось получить информацию о погоде.")

