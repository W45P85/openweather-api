import requests

API_KEY = "YOUR-KEY-HERE"
lat = "53.7912"             # Latitude of Eckernförde, Germany
lon = "9.4261"              # Longitude of Eckernförde, Germany


request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather_description = data["weather"][0]["description"]
    temparature = round(data["main"]["temp"]-273.15)
    print(f"The current weather situation is: {weather_description} at {temparature}°C")
    #print(f"{temparature}°C")
else:
    print("Abfrage nicht erfolgreich")
