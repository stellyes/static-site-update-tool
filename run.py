import PySimpleGUI as pygui
import os 

if len(os.listdir('./assets/repo')) == 0:
    print("No files found in repo directory. Please add the source code for your website and try again.")
else:

    # Create window
    window = pygui.Window(
        title="RDE Site Update Tool", 
        layout=[
            [pygui.Text("What would you like to do?", size=(30, 1), font=("Helvetica", 25))],
            [pygui.Button("Update Blog"), pygui.Button("Update Portfolio"), pygui.Button("EXIT")],
        ], 
        margins=(500, 250)
    )

    # Open window
    window.read()

    # Create event loop
    while True:
        event, values = window.read()
        if event == "OK" or event == pygui.WIN_CLOSED:
            break

    window.close()