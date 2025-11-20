import requests

def get_weather(city):
    api_key = "b43af8bcfd355ab459a5e3d982fc235b" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Build full URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Get response
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
    else:
        print("City not found!")

city_name = input("Enter city name: ")
get_weather(city_name)
