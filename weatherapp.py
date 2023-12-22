import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Use "imperial" for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = "32e81f6f88901b266cbd5b18035ec50c"
    city_name = "Philadelphia"  # Replace with the desired city

    weather_data = get_weather(api_key, city_name)

    if weather_data:
        print(f"Weather in {city_name}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        print("Unable to fetch weather data.")