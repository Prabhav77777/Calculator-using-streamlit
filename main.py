import streamlit as st
st.header("Calculator")
firstnumber=st.text_input("enter the first number")
secondnumber=st.text_input("enter the second number")
if st.button("+"):

    st.write(f"The Addition is {int(firstnumber)+int(secondnumber)}")
if st.button("-"):

    st.write(f"The subtraction is {int(firstnumber)-int(secondnumber)}")
if st.button("x"):

    st.write(f"The multiplication is {int(firstnumber)*int(secondnumber)}")
if st.button("/"):

    st.write(f"The division is {int(firstnumber)/int(secondnumber)}")