import requests 

def get_weather_desc_and_temp():
    api_key = "f37a6547370d6887a661561d1d126c5d"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = requests.json()
    print(json)

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max}

def main():
    weather_dict = get_weather_desc_and_temp()
    # print the results
    print("today's forcast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()

# Had issues downloading the requests using pip. And the entire demo needs that....
# I'm having an issue with the requests still after getting the pip figured out...
# I keep getting an error saying that there are no module named requests...

# Yup..... still not working...

