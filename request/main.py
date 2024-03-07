import requests

def fetch_weather(city):
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=YourAPIKEYq={city}"
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception if response code is not 200
        weather_data = response.json()
        print(weather_data)
        return weather_data["current"]["temp_c"], weather_data["current"]["condition"]["text"]
    except requests.exceptions.RequestException as e:
        print("Error fetching weather:", e)
        return None, None

def main():
    city = input("Enter city name: ")
    temperature, condition = fetch_weather(city)
    if temperature and condition:
        print(f"Current temperature in {city}: {temperature}°C")
        print(f"Current condition: {condition}")

if __name__ == "__main__":
    main()
