import streamlit
import streamlit as gui
from FileFunctions import  read_todos, write_todos

my_tasks = read_todos()
gui.title('My Task List')
gui.subheader("Tasks for ")
gui.write("regular lines")

for task in my_tasks:
    streamlit.checkbox(task)

gui.text_input(label='', placeholder="Add a new task...")

