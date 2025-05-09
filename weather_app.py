import requests

def get_weather(city, api_key):
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            print(f"\nWeather in {city_name}:")
            print(f"🌡 Temperature: {temp}°C")
            print(f"☁️ Description: {weather}")
            print(f"💧 Humidity: {humidity}%")
            print(f"🍃 Wind Speed: {wind} m/s")
        else:
            print("City not found. Please check the spelling.")
    except:
        print("Error fetching data. Check your internet or API key.")

# Main app
print("=== Simple Weather App ===")
city_input = input("Enter city name: ")
api_key = "956cd74f4fa0157f2db70971c6216e1a"  # Replace with your actual API key
get_weather(city_input, api_key)
