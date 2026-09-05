import streamlit as st
from todo import load_tasks, save_tasks

st.set_page_config(page_title="Todo Manager")
st.title("Todo List Manager")

tasks = load_tasks()


with st.form("task_form"):
    title = st.text_input("Task Name")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    due_date = st.date_input("Due Date")
    submitted = st.form_submit_button("Add Task")

if submitted:
    if title.strip():
        new_task = {"title": title.strip(),
                    "priority": priority,
                    "due_date": str(due_date),
                    "completed": False}
        tasks.append(new_task)
        save_tasks(tasks)
        st.success("Task added successfully!")
        st.rerun()
    else:
        st.error("Please enter a task name!")

st.divider()

filter_option = st.selectbox("Filter Tasks", ["All", "Pending", "Completed"])
st.subheader("My Tasks")

for i, task in enumerate(tasks):
    show_task = False
    
    if filter_option == "All":
        show_task = True
    elif filter_option == "Pending" and not task["completed"]:
        show_task = True
    elif filter_option == "Completed" and task["completed"]:
        show_task = True

    if show_task:
        st.write(f"### {task['title']}")
        st.write(f"**Priority:** {task['priority']}|**Due Date:** {task['due_date']}")
        
        if task["completed"]:
            st.success("Completed")
        else:
            st.warning("Pending")
                
        col_1, col_2 = st.columns(2)
        
        with col_1:
            
            if not task["completed"]:
                if st.button("Complete", key=f"complete_{i}"):
                    tasks[i]["completed"] = True
                    save_tasks(tasks)
                    st.rerun()
                    
        with col_2:
            if st.button("Delete", key=f"delete_{i}"):
                tasks.pop(i)
                save_tasks(tasks)
                st.rerun()
    
        st.divider()





