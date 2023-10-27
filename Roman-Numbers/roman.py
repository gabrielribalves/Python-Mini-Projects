import re

# As letras I, X, C podem ser escritas na frente das outras, tendo seus valores somados à letra de maior valor.
# As letras I, X, C podem ser escritas antes da outra, tendo seus valores subtraídos da letra de maior valor.



def convertRoman(userInputUpper):
    userInput = userInputUpper.lower()
    romanDict = {
        "i": 1,
        "v": 5,
        "x": 10,
        "l": 50,
        "c": 100,
        "d": 500,
        "m": 1000,
    }

    regex = "[ivxlcdm]+"
    regexFullMatch = re.fullmatch(regex, userInput)
    
    if not regexFullMatch:
        print("Por favor, digite um algarismo válido.")
        exit()

    finalNumber = 0

    for index in range(len(userInput)):
        
        before = index - 1
        nextIndex = index + 1

        actualNumber = romanDict[userInput[index]]
        beforeNumber = romanDict[userInput[before]]

        if index < len(userInput) - 1:
            nextNumber = romanDict[userInput[nextIndex]]
            # print(nextNumber)
            print(romanDict["i"])
            if (userInput[index] == "i" or userInput[index] == "x" or userInput[index] == "c") and actualNumber < nextNumber:
                finalNumber-= actualNumber
            else:
                finalNumber+= actualNumber
        else:
            finalNumber+= actualNumber
            
    return abs(finalNumber)

print(convertRoman("iv"), "-")