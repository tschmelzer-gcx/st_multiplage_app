import streamlit as st

from utils.helpers import get_baseline_input_or_fail

st.set_page_config(page_icon='✖️')

baseline = get_baseline_input_or_fail()

if baseline is None:
    st.stop()

mul = int(st.number_input("Mul value", step=1, value=1))
st.write(f"Result: {baseline * mul}")
