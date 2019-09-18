#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
These functions will be used by forecast.py
"""
import requests
#import json
from urllib3.exceptions import InsecureRequestWarning
from prettytable import PrettyTable
#from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
APIKEY = None


# to view complex dic output
def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))

# to find api key from weather.com


def setapiKey():
    global APIKEY
    ApiKey_GET = requests.get("https://weather.com/en-IN/", verify=False)
    sp = ApiKey_GET.content.decode().split("apiKey=", 1)
    sp = sp[1].split(");", 1)
    # sp[0] should have the api key
    #soup = BeautifulSoup(a.content, "lxml")
    print("Found ApiKey", "$" + sp[0] + "$")
    APIKEY = sp[0]

# finding places related to keyword entered by the user
# endpoint used: https://api.weather.com/v3/location/search


def getplaces(place):
    encode_url = {
        'apiKey': APIKEY,
        'format': 'json',
        'language': 'en-IN',
        'locationType': 'locale',
        'query': str(place)}
    searchQuery = requests.get(
        'https://api.weather.com/v3/location/search?',
        params=encode_url,
        verify=False)
    # if more than 5 entries found display top 5
    try:
        if searchQuery:

            if(len(searchQuery.json()["location"]["address"]) > 4):
                print("\nTop found places based on input argument: \t")
                for i in range(0, 5):
                    print(str(i) + ") " + searchQuery.json()
                          ["location"]["address"][i])
                print("\nPlease Select the place by entering the corresponding number: ")
                option = int(input())
                if(option < len(searchQuery.json()["location"]["address"])):
                    print("#" * 50)
                    print("Selected Place: ", searchQuery.json()
                          ["location"]["address"][option])
                    print("#" * 50)
                    return searchQuery.json()["location"]["address"][option], searchQuery.json()[
                        "location"]["placeId"][option]
                else:
                    print("Wrong Selection! try again!\n")
                    return 0

            else:
                print("\nTop found places based on input argument: \t")
                for i in range(
                    0, len(
                        searchQuery.json()["location"]["address"])):
                    print(str(i) + ") " + searchQuery.json()
                          ["location"]["address"][i])
                print("\nPlease Select the place by entering the corresponding number: ")
                option = int(input())
                if(option < len(searchQuery.json()["location"]["address"])):
                    print("Selected Place: ", searchQuery.json()
                          ["location"]["address"][option])
                    return searchQuery.json()["location"]["address"][option], searchQuery.json()[
                        "location"]["placeId"][option]
                else:
                    print("Wrong Selection! try again!\n")
                    return 0

        else:
            print("Something is not right!")
            return 0
    except BaseException:
        print("Oops!")
        return 0


# forecast display on specific date
# endpoint used: https://api.weather.com/v3/location/point and https://dsx.weather.com/wxd/v2/PastObsAvg
# first for finding coordinates of user place, second for forecast on date


def displayDateForecast(placeId, placeName, Date):
    try:
        API_PARAMS = {
            'apiKey': APIKEY,
            'format': 'json',
            'language': 'en-IN',
            'placeid': placeId
        }
        geoLocation = requests.get(
            "https://api.weather.com/v3/location/point?",
            params=API_PARAMS,
            verify=False)
        latitude = round(geoLocation.json()["location"]["latitude"], 2)
        latitude = "{0:.2f}".format(latitude)
        longitude = round(geoLocation.json()["location"]["longitude"], 2)
        longitude = "{0:.2f}".format(longitude)
        #print(Date)
        paramDate = str(Date).split("/")
        paramDate = paramDate[2] + paramDate[1] + paramDate[0]
        #print(paramDate)
        searchURL = "https://dsx.weather.com/wxd/v2/PastObsAvg/en_IN/" + \
            paramDate + "/1/" + str(latitude) + "," + str(longitude)
        # print(searchURL)
        searchQuery = requests.get(
            searchURL, params={
                'api': '7bb1c920-7027-4289-9c96-ae5e263980bc'})
        if searchQuery:
            print(
                "\nDisplaying forecast for ",
                placeName,
                " on Date",
                Date,
                "\t")
            if(len(searchQuery.content) < 10):
                print(
                    "Please Enter date between 1/1/2014 till yestarday!")
                return 0
            #print(searchQuery.content)
            table = PrettyTable(['Stats', ''])
            table.add_row(['Highest Temperature(c)',
                           searchQuery.json()[0]["Temperatures"]["highC"]])
            table.add_row(['Highest Temperature at time(ISO)',
                           searchQuery.json()[0]["Temperatures"]["highTmISO"]])
            table.add_row(['Lowest Temperature(c)',
                           searchQuery.json()[0]["Temperatures"]["lowC"]])
            table.add_row(['Lowest Temperature at time(ISO)',
                           searchQuery.json()[0]["Temperatures"]["lowTmISO"]])

            table.add_row(['Climate Condition',
                           searchQuery.json()[0]["WxDetails"]["wx"]])
            table.add_row(['Sunrise Time',
                           searchQuery.json()[0]["SunData"]["sunrise"]])
            table.add_row(['Sunset Time',
                           searchQuery.json()[0]["SunData"]["sunset"]])

            print(table)
            # print(searchQuery.json()[0])
            return 1
        else:
            return 0
    except BaseException:
        return 0


# forecast based on current(daily), hourly, 5 days, 15days
# endpoints used: https://api.weather.com/v1/geocode/ ,
# https://api.weather.com/v2/turbo/vt1observation ,
# https://api.weather.com/v2/turbo/vt1dailyForecast

def displayTypeForecast(placeId, placeName, forecastType):
    try:
        API_PARAMS = {
            'apiKey': APIKEY,
            'format': 'json',
            'language': 'en-IN',
            'placeid': str(placeId)
        }
        geoLocation = requests.get(
            "https://api.weather.com/v3/location/point?",
            params=API_PARAMS,
            verify=False)
        if geoLocation:
            latitude = round(geoLocation.json()["location"]["latitude"], 2)
            latitude = "{0:.2f}".format(latitude)
            longitude = round(geoLocation.json()["location"]["longitude"], 2)
            longitude = "{0:.2f}".format(longitude)

            # First case finding for hourly forecast
            if(forecastType == "hourly" or forecastType == "hour" or forecastType == "hours"):
                API_PARAMS = {
                    'units': 'm',
                    'language': 'en-IN',
                    'apiKey': APIKEY
                }
                timelyforecast = requests.get(
                    "https://api.weather.com/v1/geocode/" +
                    str(latitude) +
                    "/" +
                    str(longitude) +
                    "/forecast/fifteenminute.json?",
                    params=API_PARAMS)
                if timelyforecast:
                    quarterCast = timelyforecast.json()["forecasts"]
                    # print(quarterCast)
                    table = PrettyTable(['Time', 'Avg. Temp', 'Weather'])
                    for i in range(0, len(quarterCast)):
                        if(i % 4 == 0):
                            # print((quarterCast[i]["fcst_valid_local"].split("T",1)[1]).split("+",1)[0],quarterCast[i]["temp"],"\n")
                            table.add_row([(quarterCast[i]["fcst_valid_local"].split("T", 1)[1]).split(
                                "+", 1)[0], quarterCast[i]["temp"], quarterCast[i]["phrase_32char"]])
                    print("\nDisplaying hourly Forecast of ", placeName)
                    print(table)
                    return 1
                else:
                    print("Not able to fetch hour deatils.  Try again!")
                    return 0

            # Second case for Current forecast
            elif(forecastType == "current" or forecastType == "now" or forecastType == "daily"):
                API_PARAMS = {
                    'apiKey': APIKEY,
                    'format': 'json',
                    'geocode': str(latitude) + "," + str(longitude),
                    'language': 'en-IN',
                    'units': 'm'
                }
                currentForecast = requests.get(
                    "https://api.weather.com/v2/turbo/vt1observation", params=API_PARAMS)
                if currentForecast:
                    table = PrettyTable(['Stats', ''])
                    table.add_row(['Current Temperature(c)', currentForecast.json()[
                                  "vt1observation"]["temperature"]])
                    table.add_row(['Feels Like(c)', currentForecast.json()[
                                  "vt1observation"]["feelsLike"]])
                    table.add_row(['Current Humidity', currentForecast.json()[
                                  "vt1observation"]["humidity"]])
                    table.add_row(['Max Temp. since 7am', currentForecast.json()[
                                  "vt1observation"]["temperatureMaxSince7am"]])
                    table.add_row(['UV radiation', currentForecast.json()[
                                  "vt1observation"]["uvDescription"]])
                    table.add_row(['Wind Speed(km/hr)', currentForecast.json()[
                                  "vt1observation"]["windSpeed"]])
                    table.add_row(['Climate Condition', currentForecast.json()[
                                  "vt1observation"]["phrase"]])
                    print("\nDisplaying current Forecast of ", placeName)
                    print(table)
                    return 1
                else:
                    print("Not able to fetch current forecast.  Try again!")
                    return 0

            # third case for 5 days
            elif(forecastType == "5" or forecastType == 5 or forecastType == "5days" or forecastType == "five" or forecastType == "fivedays"):
                API_PARAMS = {
                    'apiKey': APIKEY,
                    'format': 'json',
                    'geocode': str(latitude) + "," + str(longitude),
                    'language': 'en-IN',
                    'units': 'm'
                }
                daysForecast = requests.get(
                    "https://api.weather.com/v2/turbo/vt1dailyForecast",
                    params=API_PARAMS)
                # print(daysForecast.json()["vt1dailyForecast"])
                if daysForecast:
                    table = PrettyTable(['Date',
                                         'Highest Temp(c)',
                                         'Lowest Temp(c)',
                                         'Climate Condition',
                                         'wind speed(km/hr)'])
                    for i in range(0, 5):
                        table.add_row(
                            [
                                daysForecast.json()["vt1dailyForecast"]["validDate"][i].split(
                                    "T",
                                    1)[0],
                                daysForecast.json()["vt1dailyForecast"]["day"]["temperature"][i],
                                daysForecast.json()["vt1dailyForecast"]["night"]["temperature"][i],
                                daysForecast.json()["vt1dailyForecast"]["day"]["phrase"][i],
                                daysForecast.json()["vt1dailyForecast"]["day"]["windSpeed"][i]])
                    print(
                        "\nDisplaying forecast of",
                        placeName,
                        " for next 5 days")
                    print(table)
                    return 1
                else:
                    print("Could not find the forecast for next few days. Try again!")
                    return 0

            # fourth case for 15 days
            elif(forecastType == "15" or forecastType == 15 or forecastType == "15days" or forecastType == "fifteen" or forecastType == "fifteendays" or forecastType == "monthly"):
                API_PARAMS = {
                    'apiKey': APIKEY,
                    'format': 'json',
                    'geocode': str(latitude) + "," + str(longitude),
                    'language': 'en-IN',
                    'units': 'm'
                }
                daysForecast = requests.get(
                    "https://api.weather.com/v2/turbo/vt1dailyForecast",
                    params=API_PARAMS)
                # print(daysForecast.json()["vt1dailyForecast"])
                if daysForecast:
                    table = PrettyTable(['Date',
                                         'Highest Temp(c)',
                                         'Lowest Temp(c)',
                                         'Climate Condition',
                                         'wind speed(km/hr)'])
                    for i in range(
                        0, len(
                            daysForecast.json()["vt1dailyForecast"]["validDate"])):
                        table.add_row(
                            [
                                daysForecast.json()["vt1dailyForecast"]["validDate"][i].split(
                                    "T",
                                    1)[0],
                                daysForecast.json()["vt1dailyForecast"]["day"]["temperature"][i],
                                daysForecast.json()["vt1dailyForecast"]["night"]["temperature"][i],
                                daysForecast.json()["vt1dailyForecast"]["day"]["phrase"][i],
                                daysForecast.json()["vt1dailyForecast"]["day"]["windSpeed"][i]])
                    print(
                        "\nDisplaying forecast of",
                        placeName,
                        " for next 15 days")
                    print(table)
                    return 1
                else:
                    print("Could not find the forecast for next 15 days. Try again!")
                    return 0
    except BaseException:
        print("Error occured! Please try again!")
        return 0
