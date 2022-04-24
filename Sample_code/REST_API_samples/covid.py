# with this API I could begin doing my own work on modeling the progression of the covid-19 pandemic

import requests
import configparser

# needed to parse ENVIRONMENT variables from config.txt
config = configparser.ConfigParser()
configFilePath = r'config.txt'
config.read(configFilePath)

# variables needed for history response
histURL = config['covid']['HIST_URL']
histQuery = {'country': 'mexico', 'day': '2020-06-02'}
# variables needed for country response
countryURL = config['covid']['CTRY_URL']
countryQuery = {}
# variables needed for stats response
statsURL = config['covid']['STATS_URL']
statsQuery = {}

# needed to make any request to the API
headers = {
    "X-RapidAPI-Host": config['covid']['API_HOST'],
    "X-RapidAPI-Key": config['covid']['API_KEY'],
}

def printHistory(histResponse):
    while histResponse:
        data = histResponse.pop()
        for key, value in data.items():
            if type(value) == dict:
                print("\n" + key.title() + ": {")
                for key, values in value.items():
                    print("\t\t" + key.title() + ": " + str(values))
                print("}")
            else:
                print("\n" + key.title() + ": " + str(value))
        print("\n\n")


history = requests.request('GET', histURL, headers=headers, params=histQuery).json()
countryInfo = ''
stats = ''

# key: 'response' has all the info we need
histResponse = history['response']
printHistory(histResponse)

# figure out a way to print a months worth of data for a list countries