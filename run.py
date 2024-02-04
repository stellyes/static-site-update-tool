import PySimpleGUI as pygui
import os 

# Create window
window = pygui.Window(
    title="RDE Site Update Tool", 
    layout=[
        [pygui.Text("Hello from PySimpleGUI")],
        [pygui.Button("OK")],
    ], 
    margins=(100, 50)
)

# Open window
window.read()

# Create event loop
while True:
    event, values = window.read()
    if event == "OK" or event == pygui.WIN_CLOSED:
        break

window.close()