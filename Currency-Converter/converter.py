#!/usr/bin/env python
"""
### Usage
py
$ converter.py --help
$ converter.py calc {first currency} {second currency} {value}
    ex: converter.py calc BRL USD 1500
$ converter.py consultCode {Name of the country}
    ex: converter.py consultCode Japan
$ converter.py consultCodeList
"""

import requests
import sys
from logging import handlers

# logging.error("Deu erro %s", str(e))

def getExchangeRate(firstCountryCode, secondCountryCode):
    url = f"https://v6.exchangerate-api.com/v6/a7103f7b0688cf42a0c649a8/latest/{firstCountryCode}"

    response = requests.get(url)
    data = response.json()
    return data['conversion_rates'][secondCountryCode]

def convertByCurrency(firstCountryCode, secondCountryCode, value):
    exchangeRate = getExchangeRate(firstCountryCode, secondCountryCode)
    resultString = f"{(value * exchangeRate):.2f}"

    return float(resultString)


def consultCode(userCountry):
    codesDict = {"United Arab Emirates":"AED","Afghanistan":"AFN","Albania":"ALL","Armenia":"AMD","Netherlands Antilles":"ANG","Angola":"AOA","Argentina":"ARS","Australia":"AUD","Aruba":"AWG","Azerbaijan":"AZN","Bosnia and Herzegovina":"BAM","Barbados":"BBD","Bangladesh":"BDT","Bulgaria":"BGN","Bahrain":"BHD","Burundi":"BIF","Bermuda":"BMD","Brunei":"BND","Bolivia":"BOB","Brazil":"BRL","Bahamas":"BSD","Bhutan":"BTN","Botswana":"BWP","Belarus":"BYN","Belize":"BZD","Canada":"CAD","Democratic Republic of the Congo":"CDF","Switzerland":"CHF","Chile":"CLP","China":"CNY","Colombia":"COP","Costa Rica":"CRC","Cuba":"CUP","Cape Verde":"CVE","Czech Republic":"CZK","Djibouti":"DJF","Denmark":"DKK","Dominican Republic":"DOP","Algeria":"DZD","Egypt":"EGP","Eritrea":"ERN","Ethiopia":"ETB","European Union":"EUR","Fiji":"FJD","Falkland Islands":"FKP","Faroe Islands":"FOK","United Kingdom":"GBP","Georgia":"GEL","Guernsey":"GGP","Ghana":"GHS","Gibraltar":"GIP","The Gambia":"GMD","Guinea":"GNF","Guatemala":"GTQ","Guyana":"GYD","Hong Kong":"HKD","Honduras":"HNL","Croatia":"HRK","Haiti":"HTG","Hungary":"HUF","Indonesia":"IDR","Israel":"ILS","Isle of Man":"IMP","India":"INR","Iraq":"IQD","Iran":"IRR","Iceland":"ISK","Jersey":"JEP","Jamaica":"JMD","Jordan":"JOD","Japan":"JPY","Kenya":"KES","Kyrgyzstan":"KGS","Cambodia":"KHR","Kiribati":"KID","Comoros":"KMF","South Korea":"KRW","Kuwait":"KWD","Cayman Islands":"KYD","Kazakhstan":"KZT","Laos":"LAK","Lebanon":"LBP","Sri Lanka":"LKR","Liberia":"LRD","Lesotho":"LSL","Libya":"LYD","Morocco":"MAD","Moldova":"MDL","Madagascar":"MGA","North Macedonia":"MKD","Myanmar":"MMK","Mongolia":"MNT","Macau":"MOP","Mauritania":"MRU","Mauritius":"MUR","Maldives":"MVR","Malawi":"MWK","Mexico":"MXN","Malaysia":"MYR","Mozambique":"MZN","Namibia":"NAD","Nigeria":"NGN","Nicaragua":"NIO","Norway":"NOK","Nepal":"NPR","New Zealand":"NZD","Oman":"OMR","Panama":"PAB","Peru":"PEN","Papua New Guinea":"PGK","Philippines":"PHP","Pakistan":"PKR","Poland":"PLN","Paraguay":"PYG","Qatar":"QAR","Romania":"RON","Serbia":"RSD","Russia":"RUB","Rwanda":"RWF","Saudi Arabia":"SAR","Solomon Islands":"SBD","Seychelles":"SCR","Sudan":"SDG","Sweden":"SEK","Singapore":"SGD","Saint Helena":"SHP","Sierra Leone":"SLE","Somalia":"SOS","Suriname":"SRD","South Sudan":"SSP","São Tomé and Príncipe":"STN","Syria":"SYP","Eswatini":"SZL","Thailand":"THB","Tajikistan":"TJS","Turkmenistan":"TMT","Tunisia":"TND","Tonga":"TOP","Turkey":"TRY","Trinidad and Tobago":"TTD","Tuvalu":"TVD","Taiwan":"TWD","Tanzania":"TZS","Ukraine":"UAH","Uganda":"UGX","United States":"USD","Uruguay":"UYU","Uzbekistan":"UZS","Venezuela":"VES","Vietnam":"VND","Vanuatu":"VUV","Samoa":"WST","CEMAC":"XAF","Organisation of Eastern Caribbean States":"XCD","International Monetary Fund":"XDR","CFA":"XOF","Collectivités d'Outre-Mer":"XPF","Yemen":"YER","South Africa":"ZAR","Zambia":"ZMW","Zimbabwe":"ZWL"}
    
    for code in codesDict:
        if code.lower() == userCountry:
            return codesDict[code]
    
    return "Country not found try \"python converter.py consultCodeList\" to see the countries and the codes"

def consultList():
    codesDict = {"United Arab Emirates":"AED","Afghanistan":"AFN","Albania":"ALL","Armenia":"AMD","Netherlands Antilles":"ANG","Angola":"AOA","Argentina":"ARS","Australia":"AUD","Aruba":"AWG","Azerbaijan":"AZN","Bosnia and Herzegovina":"BAM","Barbados":"BBD","Bangladesh":"BDT","Bulgaria":"BGN","Bahrain":"BHD","Burundi":"BIF","Bermuda":"BMD","Brunei":"BND","Bolivia":"BOB","Brazil":"BRL","Bahamas":"BSD","Bhutan":"BTN","Botswana":"BWP","Belarus":"BYN","Belize":"BZD","Canada":"CAD","Democratic Republic of the Congo":"CDF","Switzerland":"CHF","Chile":"CLP","China":"CNY","Colombia":"COP","Costa Rica":"CRC","Cuba":"CUP","Cape Verde":"CVE","Czech Republic":"CZK","Djibouti":"DJF","Denmark":"DKK","Dominican Republic":"DOP","Algeria":"DZD","Egypt":"EGP","Eritrea":"ERN","Ethiopia":"ETB","European Union":"EUR","Fiji":"FJD","Falkland Islands":"FKP","Faroe Islands":"FOK","United Kingdom":"GBP","Georgia":"GEL","Guernsey":"GGP","Ghana":"GHS","Gibraltar":"GIP","The Gambia":"GMD","Guinea":"GNF","Guatemala":"GTQ","Guyana":"GYD","Hong Kong":"HKD","Honduras":"HNL","Croatia":"HRK","Haiti":"HTG","Hungary":"HUF","Indonesia":"IDR","Israel":"ILS","Isle of Man":"IMP","India":"INR","Iraq":"IQD","Iran":"IRR","Iceland":"ISK","Jersey":"JEP","Jamaica":"JMD","Jordan":"JOD","Japan":"JPY","Kenya":"KES","Kyrgyzstan":"KGS","Cambodia":"KHR","Kiribati":"KID","Comoros":"KMF","South Korea":"KRW","Kuwait":"KWD","Cayman Islands":"KYD","Kazakhstan":"KZT","Laos":"LAK","Lebanon":"LBP","Sri Lanka":"LKR","Liberia":"LRD","Lesotho":"LSL","Libya":"LYD","Morocco":"MAD","Moldova":"MDL","Madagascar":"MGA","North Macedonia":"MKD","Myanmar":"MMK","Mongolia":"MNT","Macau":"MOP","Mauritania":"MRU","Mauritius":"MUR","Maldives":"MVR","Malawi":"MWK","Mexico":"MXN","Malaysia":"MYR","Mozambique":"MZN","Namibia":"NAD","Nigeria":"NGN","Nicaragua":"NIO","Norway":"NOK","Nepal":"NPR","New Zealand":"NZD","Oman":"OMR","Panama":"PAB","Peru":"PEN","Papua New Guinea":"PGK","Philippines":"PHP","Pakistan":"PKR","Poland":"PLN","Paraguay":"PYG","Qatar":"QAR","Romania":"RON","Serbia":"RSD","Russia":"RUB","Rwanda":"RWF","Saudi Arabia":"SAR","Solomon Islands":"SBD","Seychelles":"SCR","Sudan":"SDG","Sweden":"SEK","Singapore":"SGD","Saint Helena":"SHP","Sierra Leone":"SLE","Somalia":"SOS","Suriname":"SRD","South Sudan":"SSP","São Tomé and Príncipe":"STN","Syria":"SYP","Eswatini":"SZL","Thailand":"THB","Tajikistan":"TJS","Turkmenistan":"TMT","Tunisia":"TND","Tonga":"TOP","Turkey":"TRY","Trinidad and Tobago":"TTD","Tuvalu":"TVD","Taiwan":"TWD","Tanzania":"TZS","Ukraine":"UAH","Uganda":"UGX","United States":"USD","Uruguay":"UYU","Uzbekistan":"UZS","Venezuela":"VES","Vietnam":"VND","Vanuatu":"VUV","Samoa":"WST","CEMAC":"XAF","Organisation of Eastern Caribbean States":"XCD","International Monetary Fund":"XDR","CFA":"XOF","Collectivités d'Outre-Mer":"XPF","Yemen":"YER","South Africa":"ZAR","Zambia":"ZMW","Zimbabwe":"ZWL"}
    listOfCodes = ""
    for code in codesDict:
        listOfCodes += f"{code}: {codesDict[code]}\n"
    return listOfCodes

arg = sys.argv[1].lstrip("-")
if arg == "consultCodeList":
    print(consultList())
elif arg == "help":
    print("""\
$ converter.py calc {first currency} {second currency} {value}
    ex: converter.py calc BRL USD 1500
          
$ converter.py consultCode {Name of the country}
    ex: converter.py consultCode Japan
          
$ converter.py consultCodeList\
""")
elif arg == "consultCode":
    print(consultCode(sys.argv[2].lower()))
elif arg == "calc":
    print(convertByCurrency(sys.argv[2].upper(), sys.argv[3].upper(), float(sys.argv[4])))
else:
    print("Invalid command. Try \"converter.py --help\" for more information")