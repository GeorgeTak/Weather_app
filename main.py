
import requests


def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    if weather_data.get("cod") == 200:
        main_data = weather_data["main"]
        temperature = (main_data["temp"]-273.15)
        temp_min = (main_data["temp_min"] - 273.15)
        temp_max = (main_data["temp_max"] - 273.15)
        humidity = main_data["humidity"]
        pressure = main_data["pressure"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]
        country = weather_data["sys"]["country"]
        print(f"Country:{country}")
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Lowest temperature: {temp_min:.2f} °C")
        print(f"Highest temperature: {temp_max:.2f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure:{pressure} atm")
        print(f"Wind speed:{wind_speed} kmph")
        print(f"Description: {description}")


    if weather_data.get("cod") == "404":
        print("Unable to fetch weather data.")



api_key = "enter your api key here"

list=[]

for i in range(3):

          city = input("Enter the city you want?")
          weather_data = get_weather(api_key, city)
          display_weather(weather_data)


          list.append(i)
