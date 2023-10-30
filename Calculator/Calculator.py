import PySimpleGUI as sg
import re
import math

arrayNumber = ["0","1","2","3","4","5","6","7","8","9","√","^","%","/","*","-","+","."]

#Create a layout with Text readonly to display what the user type and the 
# buttons for the operations
layout = [
    [sg.Text(""), sg.In(key="result", enable_events=True, readonly=True, size=(30))],
    [sg.Button("√", size=(4,3)), sg.Button("^", size=(4,3)), sg.Button("%", size=(4,3)), sg.Button("C", size=(4,3))],
    [sg.Button("7", size=(4,3)), sg.Button("8", size=(4,3)), sg.Button("9", size=(4,3)), sg.Button("/", size=(4,3))],
    [sg.Button("4", size=(4,3)), sg.Button("5", size=(4,3)), sg.Button("6", size=(4,3)), sg.Button("*", size=(4,3))],
    [sg.Button("1", size=(4,3)), sg.Button("2", size=(4,3)), sg.Button("3", size=(4,3)), sg.Button("-", size=(4,3))],
    [sg.Button("test", size=(4,3)), sg.Button("0", size=(4,3)), sg.Button(".", size=(4,3)), sg.Button("+", size=(4,3))],
    [sg.Button("=", size=(8,3))],
    [sg.Button("exit", size=(4,3))],
]

window = sg.Window(title="Calculator", layout=layout, margins=(50, 50))

def updateResult(windowResult, appendValue):
    windowResult.update(f"{windowResult.get()}{appendValue}")

def printResult(windowResult):
    #If the math expression does not have Square Root or Power, it only use the
    #eval to calculate and update the Text bar, else it resolve calculation of 
    #the sqrt and pow, and replace the result in the mathExpression variable
    mathExpression = windowResult.get()
    if "√" in mathExpression:
        sqrtPattern = "\√\d+"
        allSqrt = re.findall(sqrtPattern, mathExpression)
        for sqrt in allSqrt:
            onlyNumber = sqrt[1:]
            resultSqrt = eval(f"math.sqrt({onlyNumber})")
            sqrtExpression = f"*{int(resultSqrt)}"
            mathExpression = re.sub(sqrtPattern, sqrtExpression, mathExpression, 1)
    if "^" in mathExpression:
        powPattern =  "\d+\^\d+"
        numberPattern = "\d+"
        allPow = re.findall(powPattern, mathExpression)
        for pow in allPow:
            onlyNumber = re.findall(numberPattern, pow)
            resultPow = int(eval(f"math.pow({int(onlyNumber[0])}, {int(onlyNumber[1])})"))
            mathExpression = re.sub(powPattern, str(resultPow), mathExpression, 1)

    if mathExpression[0] == "*":
        mathExpression = mathExpression[1:]

    if eval(mathExpression) % 1 == 0:
        windowResult.update(int(eval(mathExpression)))
    else:
        windowResult.update(eval(mathExpression))


while True:
    event, value = window.read()

    if event in (sg.WIN_CLOSED, "exit"):
        break
    elif event == "C":
        window["result"].update("")
    elif event in arrayNumber:
        #if the button clicked is equal one o values in array, it only append in
        #Text "result"
        updateResult(window["result"], event)
    elif event == "=":
        printResult(window["result"])

window.close()