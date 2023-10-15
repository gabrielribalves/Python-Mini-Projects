import os
import math

chosenNumber = int(input("Escolha um número: "))

numbers = ""
path = os.curdir
filePath = os.path.join(path, "numbers.txt")
with open(filePath, "r") as file_:
    numbers = file_.read() 

numbersArr = [eval(i) for i in numbers.split(",")]

upper = len(numbersArr) - 1
lower = 0

for index in range(len(numbersArr)):
    middle = math.floor((lower + upper) / 2)
    if chosenNumber > numbersArr[middle]:
        lower = middle
    elif chosenNumber < numbersArr[middle]:
        upper = middle
    else:
        print("ENCONTROU!!! 😁😁😁")
        print(f"O número {chosenNumber} está na posição {middle}")
        print(numbersArr[middle])
        break