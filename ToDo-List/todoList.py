import PySimpleGUI as sg
from todoListDB import insertInDB, deleteInDB, saveEdit, getInitialValues

td = getInitialValues()

if td == []:
    rowCount = 0
else:
    rowCount = len(td)

editIndex = 0

def reorderIndex(i, rowCount, window):
    for id in list(range(i+1, rowCount)):
        td[id-1][0] = id

    window["-TABLE-"].update(values=td)

layout = [
    [sg.CalendarButton("Set date", size=(10,1)), sg.T("-- -- -- --", key="-DATE-")],
    [
        sg.Button('ADD', k="-ADD-", size=25, button_color="green"),
        sg.Button('EDIT', k="-EDIT-", size=25, button_color="blue"),
        sg.Button('SAVE', k="-SAVE-", size=10, disabled=True),
        sg.Button('DEL', key="-DEL-",size=7, button_color="red")
    ],
    [
        sg.T("Write a Task: ", font=("None", 12)),
        sg.I(key="-TASK-", font=("None", 15), size=(32,1))
    ],
    [
        sg.Table(values=td, headings=("ID","Date","Task"),key="-TABLE-", 
                 size=(500,10), auto_size_columns=False, col_widths=(5,9,35), 
                 vertical_scroll_only=False, justification="l", 
                 font=("None, 15"))
    ],
]

window = sg.Window(title="TODO", layout=layout, margins=(10,10), size=(700,600))

#TODO Try put the delete button with the visible=False
while True:
    event, value = window.read()
    if event in (sg.WIN_CLOSED, "exit"):
        break
    if event == "-ADD-":
        rowCount += 1
        td.append([rowCount, window["-DATE-"].get().split(" ")[0], value["-TASK-"]])
        window["-TABLE-"].update(values=td)

        rowObj = {}
        rowObj["idrow"] = rowCount
        rowObj["date"] = window["-DATE-"].get().split(" ")[0]
        rowObj["task"] = value["-TASK-"]

        insertInDB(rowObj)
        window["-TASK-"].update(value="")

    if event == ("-DEL-"):
        if value["-TABLE-"] != []:
            i = value["-TABLE-"][0]
            popupAnswer = sg.popup_yes_no("Are you sure?")
            if(popupAnswer == "Yes"):
                del td[i]
                window["-TABLE-"].update(values=td)
                deleteInDB(i + 1)
                reorderIndex(i, rowCount, window)
                rowCount -= 1
    if event == ("-EDIT-"):
        editIndex = value["-TABLE-"][0]
        window["-SAVE-"].update(disabled=False)
        window["-TASK-"].update(value=td[editIndex][2])
        window["-DATE-"].update(value=td[editIndex][1])
        td[editIndex][2] = ""
        td[editIndex][1] = ""
        window["-TABLE-"].update(values=td)

        window["-ADD-"].update(disabled=True)
        window["-EDIT-"].update(disabled=True)
        window["-DEL-"].update(disabled=True)
    if event == ("-SAVE-"):
        td[editIndex][2] = window["-TASK-"].get()
        td[editIndex][1] = window["-DATE-"].get().split(" ")[0]
        window["-TABLE-"].update(values=td)
        window["-TASK-"].update(value="")
        window["-TASK-"].update(value="")
        window["-SAVE-"].update(disabled=True)
        window["-ADD-"].update(disabled=False)
        window["-EDIT-"].update(disabled=False)
        window["-DEL-"].update(disabled=False)
        saveEdit(editIndex + 1, td[editIndex][1], td[editIndex][2])



window.close()