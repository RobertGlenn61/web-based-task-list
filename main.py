import streamlit
import streamlit as gui
from FileFunctions import  read_todos, write_todos


my_tasks = read_todos()

def add_task():
    task = gui.session_state['new_task'] + '\n'
    my_tasks.append(task)
    write_todos(my_tasks)
    gui.session_state['new_task'] = ''


gui.title('My Task List')
gui.subheader("Tasks for ")
gui.write("regular lines")

for task in my_tasks:
    streamlit.checkbox(task)

gui.text_input(label='', placeholder="Add a new task...",
               on_change=add_task, key='new_task')

