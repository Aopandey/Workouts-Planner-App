import functions
import PySimpleGUI as zx
import time
import os

if not os.path.exists('Workouts.txt'):
    with open('Workouts.txt', 'w') as file:
        pass

zx.theme('DarkBlack')

clock = zx.Text('',key='clock')
label = zx.Text("Type in your Workouts")
input_box = zx.InputText(tooltip="Enter an exercise",
                         key="Exercise")
add_button = zx.Button(image_source='add.png', tooltip='Add an exercise', key='Add')
list_box = zx.Listbox(values=functions.get_workouts(), key='Exercises',
                      enable_events=True, size=[38, 10])
edit_button = zx.Button("Edit")
complete_button = zx.Button(image_source='complete.png', tooltip='Click on an exercise that you completed',
                            key='Complete')
exit_button = zx.Button("Exit")

window = zx.Window('My Workout Planner App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=250)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            workouts = functions.get_workouts()
            new_workout = values['Exercise'] + '\n'
            workouts.append(new_workout)
            functions.write_workouts(workouts)
            window['Exercises'].update(values=workouts)
        case "Edit":
            try:
                Exercise_to_edit = values['Exercises'][0]
                new_exercises = values['Exercise']

                workouts = functions.get_workouts()
                index = workouts.index(Exercise_to_edit)
                workouts[index] = new_exercises
                functions.write_workouts(workouts)
                window['Exercises'].update(values=workouts)
            except IndexError:
                zx.popup("Please select an exercise first.")
        case 'Complete':
            try:
                Exercise_to_complete = values['Exercises'][0]
                workouts = functions.get_workouts()
                workouts.remove(Exercise_to_complete)
                functions.write_workouts(workouts)
                window['Exercises'].update(values=workouts)
                window['Exercise'].update(value='')
            except IndexError:
                zx.popup("Please select an exercise first.")
        case 'Exit':
            break
        case 'Exercises':
            window['Exercise'].update(value=values['Exercises'][0])
        case zx.WIN_CLOSED:
            break

window.close()



