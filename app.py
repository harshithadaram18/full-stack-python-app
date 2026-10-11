import streamlit as st

st.set_page_config(page_title="Full Stack Python App")

st.title("Full Stack Python App")
st.subheader("Student Task Manager")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter your task")

if st.button("Add Task"):
    if task.strip():
        st.session_state.tasks.append({
            "task": task.strip(),
            "completed": False
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

st.write("### My Tasks")

for i, item in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.write(item["task"])

    with col2:
        if not item["completed"]:
            if st.button("Complete", key=f"complete_{i}"):
                item["completed"] = True
                st.rerun()
        else:
            st.write("Done ✅")

    with col3:
        if st.button("Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
          
