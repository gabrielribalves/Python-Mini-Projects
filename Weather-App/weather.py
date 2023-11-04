#!/usr/bin/env python
"""
### Usage
py
$ weather.py --help
$ weather.py {city} {state} {country}
    The city anc state are optional
    ex: $ weather.py BRA SP Maua
    ex: $ weather.py BRA

    Expected return:
        Temperature: 21.19
        Feels Like: 21.74
        Min Temperature: 17.83
        Max Temperature: 25.76
"""
import requests
import sys
from logging import handlers

key = "4a3326e4b0c3d47de892930ab4bb5431"

def getLatLon(country:str, complement:list)-> dict:
    returnObj = {
        "lat":"",
        "lon":""
    }
    url = ""
    if complement:
        state, city = complement
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&&appid={key}"
    else:
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={country}&&appid={key}"
    
    response = requests.get(url)
    data = response.json()[0]

    returnObj["lat"] = data["lat"]
    returnObj["lon"] = data["lon"]
    return returnObj


def getWeather(country:str, *complement):
    location = getLatLon(country, complement)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location['lat']}&lon={location['lon']}&appid={key}&units=metric"
    response = requests.get(url)
    data = response.json()

    print(f"""\
Temperature: {data["main"]["temp"]}
Feels Like: {data["main"]["feels_like"]}
Min Temperature: {data["main"]["temp_min"]}
Max Temperature: {data["main"]["temp_max"]}\
""")

args = sys.argv[1:]

if len(args) > 1:
    getWeather(args[0], args[1], args[2])
else:
    getWeather(args[0])
