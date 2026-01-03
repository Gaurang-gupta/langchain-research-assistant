import streamlit as st

def render_ui():
    st.title("AI Research & Decision Assistant")
    query = st.text_input("Enter your research query")

    if query:
        st.info("Processing pipeline not connected yet")

if __name__ == "__main__":
    render_ui()
