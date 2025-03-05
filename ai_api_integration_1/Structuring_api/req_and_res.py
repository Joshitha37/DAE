import requests
# API Key from OpenWeatherMap
api_key = "2c092f21a51382613972ad3af022d0e7" 
city = "Orlando"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get (url)

if response.status_code == 200:
    data = response. json()
    weather_description = data[ 'weather'] [0] ['description']
    temperature = data ['main'] ['temp']
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")
    weather_description = "Error fetching weather data."
    temperature = "N/A"