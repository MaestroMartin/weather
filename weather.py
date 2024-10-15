from pprint import pprint  # Import pprint for better display of JSON responses

import requests  # Import requests to handle API calls

# API key for OpenWeatherMap (replace 'enter here your api key' with your actual API key)
api_key = "enter here your api key"

# Base URL for the OpenWeatherMap API
Base_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Define the city for which the weather data is requested
City = "Brno"

# Build the complete URL for the API request, including the city and API key
# Make sure to use the actual variable for 'api_key', not the string 'api_key'
url = Base_URL + "appid=" + api_key + "&q=" + City + "&units=metric"

# Send a request to the API and convert the response to JSON
response = requests.get(url).json()

# Print the raw JSON response
print(response)

# Pretty-print the JSON response for better readability
pprint(response)


