import functions
import PySimpleGUI as zx

label = zx.Text("Type in your Workouts")
input_box = zx.InputText(tooltip="Enter an exercise",
                         key="Exercise")
add_button = zx.Button("Add")
list_box = zx.Listbox(values=functions.get_workouts(), key='Exercises',
                      enable_events=True, size=[38, 8])
edit_button = zx.Button("Edit")

window = zx.Window('My Workout Planner App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Times new roman', 12))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['Exercises'])
    match event:
        case "Add":
            workouts = functions.get_workouts()
            new_workout = values['Exercise'] + '\n'
            workouts.append(new_workout)
            functions.write_workouts(workouts)
            window['Exercises'].update(values=workouts)
        case "Edit":
            Exercise_to_edit = values['Exercises'][0]
            new_exercises = values['Exercise']

            workouts = functions.get_workouts()
            index = workouts.index(Exercise_to_edit)
            workouts[index] = new_exercises
            functions.write_workouts(workouts)
            window['Exercises'].update(values=workouts)
        case 'Exercises':
            window['Exercise'].update(value=values['Exercises'][0])
        case zx.WIN_CLOSED:
            break

window.close()



