import streamlit as zx
import functions

workouts = functions.get_workouts()

zx.title("My Workout Planner App")
zx.write("This app is for you to plan out your workouts.")

for workout in workouts:
    zx.checkbox(workout)

zx.text_input(label='', placeholder='Add an exercise...')
