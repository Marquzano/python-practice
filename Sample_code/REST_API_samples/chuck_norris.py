# here I am working on retrieving JSON data from a free api
import requests
import configparser

# we'll be reading the needed variables like URL, API_KEY, and API_HOST from a config file
config = configparser.ConfigParser()
configFilePath = r'config.txt'
config.read(configFilePath)

# this url looks to be the 
url = config['chuck-norris-config']['URL']

headers = {
    "accept": 'aplication/json',
    "X-RapidAPI-Host": config['chuck-norris-config']['API_HOST'],
    "X-RapidAPI-Key": config['chuck-norris-config']['API_KEY'],
}

response = requests.request("GET", url, headers=headers)

print(response.status_code) # gives 406 status code, will move on to another API for now