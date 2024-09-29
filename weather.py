from pprint import pprint

import requests

city = "Brno "

Base_URL = "https://api.openweathermap.org/data/2.5/weather?"
City = "Brno"

url = Base_URL + "appid=" + "api_key" + "&q=" + City + "&units=metric"

response = requests.get(url).json()

print(response)

pprint(response)

