import streamlit as st

def get_baseline_input_or_fail(key: str = "num") -> int:
    if not key in st.session_state:
        st.warning("Please provide a baseline number at the main page first!")
    else:
        return st.session_state[key]
