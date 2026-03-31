import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.title("📅 Appointment Booking System")

menu = ["Register", "Login", "Book Appointment", "View Appointments"]
choice = st.sidebar.selectbox("Menu", menu)

# ------------------ REGISTER ------------------
if choice == "Register":
    st.subheader("Create Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        res = requests.post(f"{API_URL}/register", json={
            "name": name,
            "email": email,
            "password": password
        })
        st.success(res.json()["message"])


# ------------------ LOGIN ------------------
elif choice == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(f"{API_URL}/login", json={
            "email": email,
            "password": password
        })

        if res.status_code == 200:
            st.success(res.json()["message"])
        else:
            st.error(res.json()["message"])


# ------------------ BOOK APPOINTMENT ------------------
elif choice == "Book Appointment":
    st.subheader("Book Appointment")

    name = st.text_input("Your Name")
    date = st.date_input("Select Date")
    time = st.selectbox("Select Time", ["10:00", "12:00", "14:00", "16:00"])

    if st.button("Book Appointment"):
        res = requests.post(f"{API_URL}/book", json={
            "name": name,
            "date": str(date),
            "time": time
        })

        if res.status_code == 200:
            st.success(res.json()["message"])
        else:
            st.error(res.json()["message"])


# ------------------ VIEW APPOINTMENTS ------------------
elif choice == "View Appointments":
    st.subheader("All Appointments")

    res = requests.get(f"{API_URL}/appointments")
    data = res.json()

    if len(data) == 0:
        st.warning("No appointments found")
    else:
        for appt in data:
            st.write(f"👤 {appt['name']} | 📅 {appt['date']} | ⏰ {appt['time']}")
