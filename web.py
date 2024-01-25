import streamlit as st
import functions

todos = functions.get_todos()


def new_todo():
    todo = st.session_state['todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("My Todo Abb")
st.subheader('this is my todo app')
st.write('This app is to increase your productivity')

for j, i in enumerate(todos):
    check = st.checkbox(i, key=i)
    if check:
        todos.pop(j)
        functions.write_todos(todos)
        del st.session_state[i]
        st.experimental_rerun()

st.text_input('Enter a todo', placeholder="Add new todo...",
              on_change=new_todo, key='todo')
