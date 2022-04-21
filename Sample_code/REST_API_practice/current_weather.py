import requests
import configparser

config = configparser.ConfigParser()
configFilePath = r'config.txt'
config.read(configFilePath)

url = config['weather']['URL']

headers = {
    'X-RapidAPI-Host': config['weather']['API_HOST'],
    'X-RapidAPI-Key': config['weather']['API_KEY'],
}

queryString = {
    'q': "Nashville,us",
    'mode': "json",
    'units': 'imperial',
}

# adding .json() method makes a JSON object into a Python/Dict object
response = requests.request("GET", url, headers=headers, params=queryString).json()

main_weather = response['weather'][0]['main']
description = response['weather'][0]['description']
main_temp = str(response['main']['temp'])
feels_like = str(response['main']['feels_like'])
min_temp = str(response['main']['temp_min'])
max_temp = str(response['main']['temp_max'])
country = response['sys']['country']
city = response['name']

print("Here is the weather for " + city.title() + ", " + country.upper() + ":")
print("The overall weather for today is " + main_weather.title() + " described as " + description.title() + ".")
print("Here is the list of temperatures for the day:")
print("\t main: " + main_temp)
print("\t min: " + min_temp)
print("\t max: " + max_temp)
print("Overall it will feel like: " + feels_like)
# I want to be able to parse and print the data I wish to see
# I want the following
# "weather": [{"main":, "description":,}]
# "main": {"temp":, "feels_like":, "temp_min":, "temp_max":,}
# "sys": {"country":,}
# "name": ""