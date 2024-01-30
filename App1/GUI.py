import functions
import PySimpleGUI as zx

label = zx.Text("Type in your Workouts")
input_box = zx.InputText(tooltip="Enter an exercise",
                         key="Exercise")
add_button = zx.Button("Add")

window = zx.Window('My Workout Planner App',
                   layout=[[label], [input_box, add_button]],
                   font=('Times new roman', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            workouts = functions.get_workouts()
            new_workout = values['Exercise'] + '\n'
            workouts.append(new_workout)
            functions.write_workouts(workouts)
        case zx.WIN_CLOSED:
            break

window.close()



