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

response = requests.request("GET", url, headers=headers, params=queryString)

print(response.text) # I am printing it as text here

# I want to be able to parse and print the data I wish to see
# I want the following
# "weather": [{"main":, "description":,}]
# "main": {"temp":, "feels_like":, "temp_min":, "temp_max":,}
# "sys": {"country":,}
# "name": ""