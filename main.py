import PySimpleGUI as sg
from components import appDetector, vsStart

layout = [[sg.Text("Projects")],
    [sg.Button("open", key="-OP-"), sg.Button("new", key="-NEW-"), sg.Button("manage")]
]

window = sg.Window("Projects - BatApp Creator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-OP-":
        os.system("explorer.exe")
        sg.popup("Not full implemented yet")
        vsStart.start(".")

    if event == "-NEW-":
        sg.popup("Not implemented yet")

    if event == "manage":
        sg.popup("Not implemented yet")
window.close()
