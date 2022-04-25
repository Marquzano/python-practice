# with this API I could begin doing my own work on modeling the progression of the covid-19 pandemic :o

from time import time
import requests
import configparser
import json

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

# the dumps() method makes my printHistory function obsolete...
# def printHistory(histResponse):
#     while histResponse:
#         data = histResponse.pop()
#         for key, value in data.items():
#             if type(value) == dict:
#                 print("\n" + key.title() + ": {")
#                 for key, values in value.items():
#                     print("\t\t" + key.title() + ": " + str(values))
#                 print("}")
#             else:
#                 print("\n" + key.title() + ": " + str(value))
#         print("\n\n")


history = requests.request('GET', histURL, headers=headers, params=histQuery).json()
countryInfo = ''
stats = ''

text = json.dumps(history, sort_keys=True, indent=4)
# print(text)
# key: 'response' has all the info we need
# histResponse = history['response']
# printHistory(histResponse)

# figure out a way to print a months worth of data for a list countries

# if I wanted to report on the new highest recovery count and give the time how would I do that?

def timeOfMostRecovered(history):
    timeMostRecovered = ''
    histResponses = history['response']
    while histResponses:
        review = histResponses.pop()
        reviewed = []
        recovered = {}
        recovered[review['cases']['recovered']] = review['time']
        reviewed.append(review)
    timeMostRecovered = recovered[max(recovered)]
    return timeMostRecovered

result = timeOfMostRecovered(history)
print(result)

