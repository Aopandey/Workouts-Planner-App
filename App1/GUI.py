import PySimpleGUI as zx

label = zx.Text("Type in your Workouts")
input_box = zx.InputText(tooltip="Enter an exercise")
add_button = zx.Button("Add")

window = zx.Window('My Workout Planner App', layout=[[label], [input_box, add_button]])
window.read()
window.close()



