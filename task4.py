# pip install requests
import requests
import json

API_KEY = "YOUR_API_KEY"

def fetch_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather_data(data):
    # Parse and display weather data (e.g., temperature, humidity, wind speed, etc.)
    pass

def main():
    print("Welcome to the Weather App!")

    while True:
        location = input("Enter a location (or 'q' to quit): ")
        if location.lower() == 'q':
            print("Thank you for using the Weather App. Goodbye!")
            break

        weather_data = fetch_weather_data(location)
        if 'main' in weather_data and 'weather' in weather_data:
            display_weather_data(weather_data)
        else:
            print("Location not found. Please try again.")

if __name__ == "__main__":
    main()

