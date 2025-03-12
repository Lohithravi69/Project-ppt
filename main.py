import requests
import argparse

API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.json().get('message', 'Unable to fetch weather data')}")

def main():
    parser = argparse.ArgumentParser(description='Get the current weather for a given city.')
    parser.add_argument('city', type=str, help='Name of the city to get the weather for')
    args = parser.parse_args()
    get_weather(args.city)

if __name__ == '__main__':
    main()