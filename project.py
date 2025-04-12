import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"Current weather in {city}: {temp}°C, {weather}")
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather')}")

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key_here"
city_name = input("Enter a city: ")
get_weather(city_name, API_KEY)
