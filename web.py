import streamlit as st
import functions as func

# Get ToDos list from todos.txt file
todos_list = func.get_list_from_textfile()


# Functions
def add_todo():
    """
    This function adds the new item to list from text input box
    and saves new list to todos.txt file.
    :return: None
    """
    new_todo = st.session_state["todo_input"]
    if new_todo != "":
        todos_list.append(new_todo)
        func.save_list_to_file(todos_list)
    st.session_state["todo_input"] = ""


def clear_list():
    """
    Clears the list and saves the empty list to the todos.txt file
    :return: None
    """
    todos_list.clear()
    func.save_list_to_file(todos_list)


st.title("Check List")
st.subheader("My tasks:")

for index, todo in enumerate(todos_list):
    new_key = todo + str(index)
    checkbox = st.checkbox(todo, key=new_key)
    if checkbox:
        del todos_list[index]
        func.save_list_to_file(todos_list)
        del st.session_state[new_key]
        st.rerun()

st.text_input(label="Textbox", label_visibility="hidden",
              placeholder="Write your todo here...",
              on_change=add_todo, key="todo_input")

st.button("Clear", on_click=clear_list, help="Remove all items from the list")
