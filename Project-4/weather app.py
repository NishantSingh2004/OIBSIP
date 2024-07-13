import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if data.get('cod') != 200:
        print(f"Error fetching weather data: {data.get('message')}")
        return

    city = data.get('name')
    weather_desc = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    print(f"Weather in {city}:")
    print(f"Condition: {weather_desc}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")

def main():
    api_key = "e0672066103cf9c8a2dec3afce7860ac"  # Replace with your actual API key
    location = input("Enter the city or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
