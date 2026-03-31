import streamlit as st
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "YOUR_MONGO_URI"
client = MongoClient(MONGO_URI)
db = client["appointment_db"]

users_collection = db["users"]
appointments_collection = db["appointments"]

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
        users_collection.insert_one({
            "name": name,
            "email": email,
            "password": password
        })
        st.success("User registered successfully")


# ------------------ LOGIN ------------------
elif choice == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = users_collection.find_one({
            "email": email,
            "password": password
        })

        if user:
            st.success("Login successful")
        else:
            st.error("Invalid credentials")


# ------------------ BOOK APPOINTMENT ------------------
elif choice == "Book Appointment":
    st.subheader("Book Appointment")

    name = st.text_input("Your Name")
    date = st.date_input("Select Date")
    time = st.selectbox("Select Time", ["10:00", "12:00", "14:00", "16:00"])

    if st.button("Book Appointment"):
        existing = appointments_collection.find_one({
            "date": str(date),
            "time": time
        })

        if existing:
            st.error("Slot already booked")
        else:
            appointments_collection.insert_one({
                "name": name,
                "date": str(date),
                "time": time
            })
            st.success("Appointment booked successfully")


# ------------------ VIEW APPOINTMENTS ------------------
elif choice == "View Appointments":
    st.subheader("All Appointments")

    data = list(appointments_collection.find({}, {"_id": 0}))

    if len(data) == 0:
        st.warning("No appointments found")
    else:
        for appt in data:
            st.write(f"👤 {appt['name']} | 📅 {appt['date']} | ⏰ {appt['time']}")
