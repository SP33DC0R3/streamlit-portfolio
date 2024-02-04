import streamlit as sl

sl.header("Contact Us")

with sl.form(key="email_form"):
    user_email = sl.text_input("Your email:")
    message = sl.text_area("Your Message:")
    button = sl.form_submit_button("Send")
    if button:
        print("Hello")