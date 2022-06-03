import streamlit as st

st.set_page_config(page_icon='🔢')

st.markdown("# Calculator App")
st.markdown("#### Please provide a baseline number")

num = int(st.number_input("Baseline", value=42, step=1))
st.session_state["num"] = num
