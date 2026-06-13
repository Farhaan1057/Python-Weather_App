# ERROR 1 IN GEOPY 

    # geolocator = Nominatim(user_agent="your_app_name", timeout=10)
    # print(f"Searching for: {city}")
    # location = geolocator.geocode(city)
    
# THE ERROR WAS THE HTTPS SERVER 403 ERROR AND COULD NOT FETCH DATA FROM THE API NOMINATIM BUT RESOLVED BY SETTING A timeout=10.

# ERROR 2 SOLVED 

# ACTUAL CODE 

 # WEATHER 
    
    # api = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ed49a0f86a6af09e4c3c2937966c136e"
    
    # json_data = requests.get(api).json()
    # condition = json_data['weather'][0]['main']
    # description = json_data['weather'][0]['description']
    # temp = int(json_data['main']['temp'] -273.15)
    # pressure = json_data['main']['pressure']
    # humidity = json_data['main']['humidity']
    # wind = json_data['wind']['speed']
    
    # t.config(text=(temp, "°"))
    # c.config(text = (condition, "⏐", "FEELS", "LIKE", temp, "°"))
    
# revised code

# WEATHER 
    
    # api = "https://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=ed49a0f86a6af09e4c3c2937966c136e"
    
    # json_data = requests.get(api).json()
    # condition = json_data['weather'][0]['main']
    # description = json_data['weather'][0]['description']
    # temp = int(json_data['main']['temp'] -273.15)
    # pressure = json_data['main']['pressure']
    # humidity = json_data['main']['humidity']
    # wind = json_data['wind']['speed']
    
    # t.config(text=(temp, "°"))
    # c.config(text = (condition, "⏐", "FEELS", "LIKE", temp, "°"))