import streamlit as st
import pandas as pd
from send_email import send_email

st.set_page_config(page_title="Contact Us", page_icon="📬", layout="centered")

st.title("📬 Contact Us")
st.write("Have a question or proposal? Fill out the form below and we'll get back to you.")

topics = pd.read_csv("topics.csv")["topic"].tolist()

with st.form("contact_form"):
    user_name = st.text_input("Your Name")
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox("Topic", topics)
    raw_message = st.text_area("Your Message", height=150)
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if not user_name or not user_email or not raw_message:
            st.error("Please fill in all fields before submitting.")
        elif "@" not in user_email:
            st.error("Please enter a valid email address.")
        else:
            message = f"""\
Subject: [{topic}] from {user_name}

From: {user_name} <{user_email}>
Topic: {topic}

{raw_message}
"""
            try:
                send_email(message)
                st.success("✅ Your message has been sent successfully! We'll be in touch soon.")
            except Exception as e:
                st.error(f"Failed to send email: {e}")
