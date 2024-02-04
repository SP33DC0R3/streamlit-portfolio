import streamlit as sl
from send_email import send_email

sl.header("Contact Us")

with sl.form(key="email_form"):
    user_email = sl.text_input("Your email:")
    raw_message = sl.text_area("Your Message:")
    message = f"""\
    Subject: Python Portfolio Message
    
    From: {user_email}
    {raw_message}
"""
    button = sl.form_submit_button("Send")
    if button:
        send_email(message)
        sl.info("Your email was sent!")