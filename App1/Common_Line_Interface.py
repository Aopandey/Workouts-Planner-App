from App1 import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    exercises = input("Type add, show, edit, complete or exit: ")
    exercises = exercises.strip()

    if exercises.startswith('add'):
        exercise = exercises[4:] + '\n'

        Workouts = functions.get_workouts()

        Workouts.append(exercise)

        functions.write_workouts(Workouts)

    elif exercises.startswith('show'):
        Workouts = functions.get_workouts()

        for index, item in enumerate(Workouts):
            item = item.strip('\n')
            row = f'{index + 1}. {item}'
            print(row)
    elif exercises.startswith('edit'):
        try:
            muscle = int(exercises[5:])
            muscle = muscle - 1

            Workouts = functions.get_workouts()

            new_exercise = input("Enter a new workout: ")
            Workouts[muscle] = new_exercise + '\n'

            functions.write_workouts(Workouts)

        except ValueError:
            print("Your command is not valid")
            continue

    elif exercises.startswith('complete'):
        try:
            number = int(exercises[9:])

            Workouts = functions.get_workouts()
            index = number - 1
            exercise_remove = Workouts[index].strip('\n')
            Workouts.pop(index)

            functions.write_workouts(Workouts)

            message = f"Exercise {exercise_remove} was completed"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif exercises.startswith('exit'):
        break

    else:
        print("Nuh uh lil bro")
    # if _ in exercises:
    #     print("Nuh uh lil bro")

print('Thank you!')
