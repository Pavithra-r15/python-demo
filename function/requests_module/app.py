import requests

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "error" not in data:
        temperature = data["current"]["temp_c"]
        wind_direction = data["current"]["wind_degree"]
        humidity = data["current"]["humidity"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Direction: {wind_direction}°")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or some other error occurred.")
 
api_key = "475f71268bfe4af89fd65418242803"
city = "Trichy" 

get_weather(api_key, city)
