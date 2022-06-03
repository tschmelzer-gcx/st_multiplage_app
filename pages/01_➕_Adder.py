from email.mime import base
import streamlit as st

from utils.helpers import get_baseline_input_or_fail

st.set_page_config(page_icon='➕')

baseline = get_baseline_input_or_fail()

if baseline is None:
    st.stop()

add = int(st.number_input("Add value", step=1))
st.write(f"Result: {baseline + add}")
