import requests

city = "Brno "

Base_URL = "https://api.openweathermap.org/data/2.5/weather?"
City = "Brno"

url = Base_URL + "appid=" + "ed780eb9027702dbd34f95f4c86b7cef" + "&q=" + City + "&units=metric"

response = requests.get(url).json()

print(response)

