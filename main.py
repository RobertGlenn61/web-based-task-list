import streamlit
import streamlit as gui
from FileFunctions import  read_todos, write_todos


my_tasks = read_todos()

def add_task():
    task = gui.session_state['new_task'] + '\n'
    my_tasks.append(task)
    write_todos(my_tasks)
    del gui.session_state['new_task']


gui.title('My Task List')
gui.subheader("Tasks for ")
gui.write("regular lines")

for index, task in enumerate(my_tasks):
    checkbox = streamlit.checkbox(task, key=task)
    if checkbox:
        my_tasks.pop(index)
        write_todos(my_tasks)
        del gui.session_state[task]
        gui.rerun()

gui.text_input(label='', placeholder="Add a new task...",
               on_change=add_task, key='new_task')

