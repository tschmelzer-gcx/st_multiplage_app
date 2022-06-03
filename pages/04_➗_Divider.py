import streamlit as st

from utils.helpers import get_baseline_input_or_fail

baseline = get_baseline_input_or_fail()

st.set_page_config(page_icon='➗')

if baseline is None:
    st.stop()

div = st.number_input("Div value", value=1, step=1)
if div == 0:
    st.warning("Cannot divide by 0. Please provide another value.")
    st.stop()

st.write(f"Result: {baseline / div}")
