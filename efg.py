import streamlit as st

# Function to add a task
def add_task():
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []
    task = st.session_state['task_input']
    if task:
        st.session_state['tasks'].append(task)
        st.session_state['task_input'] = ""  # Clear the input field

# Function to delete a task
def delete_task(task_index):
    if 'tasks' in st.session_state:
        st.session_state['tasks'].pop(task_index)

# Function to clear all tasks
def clear_tasks():
    st.session_state['tasks'] = []

def main():
    st.title("To-Do List")

    # Input field for new tasks
    task_input = st.text_input("Enter a task", key='task_input')
    st.button("Add Task", on_click=add_task)

    # Display tasks
    if 'tasks' in st.session_state and st.session_state['tasks']:
        for i, task in enumerate(st.session_state['tasks']):
            col1, col2 = st.columns([0.9, 0.1])
            col1.write(task)
            col2.button("Delete", key=f"delete_{i}", on_click=delete_task, args=(i,))

    # Clear tasks button
    st.button("Clear List", on_click=clear_tasks)

if __name__ == "__main__":
    main()
