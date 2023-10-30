import PySimpleGUI as sg
import re
import math

class Calculator:
    def __init__(self):
        self.window = sg.Window(title="Calculator", layout=self.create_layout(), margins=(50, 50))

    def create_layout(self):
        layout = [
            [sg.Text(""), sg.In(key="result", enable_events=True, readonly=True, size=(30))],
            [sg.Button("√", size=(4, 3)), sg.Button("^", size=(4, 3)), sg.Button("%", size=(4, 3)), sg.Button("C", size=(4, 3))],
            [sg.Button("7", size=(4, 3)), sg.Button("8", size=(4, 3)), sg.Button("9", size=(4, 3)), sg.Button("/", size=(4, 3))],
            [sg.Button("4", size=(4, 3)), sg.Button("5", size=(4, 3)), sg.Button("6", size=(4, 3)), sg.Button("*", size=(4, 3))],
            [sg.Button("1", size=(4, 3)), sg.Button("2", size=(4, 3)), sg.Button("3", size=(4, 3)), sg.Button("-", size=(4, 3))],
            [sg.Button("", size=(4, 3)), sg.Button("0", size=(4, 3)), sg.Button(".", size=(4, 3)), sg.Button("+", size=(4, 3))],
            [sg.Button("=", size=(8, 3))],
            [sg.Button("exit", size=(4, 3))],
        ]

        return layout

    def update_result(self, append_value):
        current_text = self.window["result"].get()
        self.window["result"].update(f"{current_text}{append_value}")

    def print_result(self):
        math_expression = self.window["result"].get()
        # Rest of your calculation logic here...

    def run(self):
        arrayNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "√", "^", "%", "/", "*", "-", "."]
        while True:
            event, value = self.window.read()
            if event in (sg.WIN_CLOSED, "exit"):
                break
            elif event == "C":
                self.window["result"].update("")
            elif event in arrayNumber:
                self.update_result(event)
            elif event == "=":
                self.print_result()

        self.window.close()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
