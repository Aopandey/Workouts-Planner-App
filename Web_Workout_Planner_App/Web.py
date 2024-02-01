import streamlit as zx
import functions

workouts = functions.get_workouts()


def add_workout():
    workout = zx.session_state['new_workout'] + '\n'
    workouts.append(workout)
    functions.write_workouts(workouts)


zx.title("My Workout Planner App")
zx.write("This app is for you to plan out your workouts.")

for index, workout in enumerate(workouts):
    checkbox = zx.checkbox(workout, key=workout)
    if checkbox:
        workouts.pop(index)
        functions.write_workouts(workouts)
        del zx.session_state[workout]
        zx.rerun()

zx.text_input(label='', placeholder='Add an exercise...',
              on_change=add_workout, key='new_workout')
