import streamlit as st

st.header("Calculator")
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.00)
with col2:
    num2 = st.number_input("Enter second number", value=0.00)

col1, col2, col3, col4 = st.columns(4)

result = None

with col1:
    if st.button("+"):
        result = num1 + num2
with col2:
    if st.button("-"):
        result = num1 - num2
with col3:
    if st.button("x"):
        result = num1 * num2
with col4:
    if st.button("÷"):
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error"
        

if result is not None:
    st.success(f"Result:{result}")

