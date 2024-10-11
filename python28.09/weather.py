import requests

def get_weather(city, api_key):
    # Базовый URL для запроса
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Параметры запроса
    params = {
        'q': city,           
        'appid': api_key,    
        'units': 'metric',   
        'lang': 'ru'         
    }

    try:
        # Выполнение GET-запроса
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Проверка на наличие HTTP-ошибок
        weather_data = response.json()  # Преобразование ответа в JSON

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
        print(f"HTTP Error: {errh}")  # Обработка HTTP-ошибок
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")  # Ошибка подключения
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")  # Ошибка тайм-аута
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")  # Другие ошибки запроса
    except KeyError:
        print("Не удалось получить данные о погоде. Проверьте название города.")  # Ошибка при отсутствии ключевых данных

if __name__ == "__main__":
    api_key = "2e701822db143ee888636fd324905449"   # Ключ API 
    city = input("Введите название города: ") 
    get_weather(city, api_key)  
