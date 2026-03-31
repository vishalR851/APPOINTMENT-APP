import streamlit as st

st.set_page_config(page_title="Appointment App", page_icon="📅")

# Temporary storage
if "users" not in st.session_state:
    st.session_state.users = {}

if "appointments" not in st.session_state:
    st.session_state.appointments = []

# Sidebar
menu = st.sidebar.selectbox("Menu", ["Register", "Login", "Book Appointment", "View Appointments"])

st.title("📅 Appointment Booking System")

# ---------------- REGISTER ----------------
if menu == "Register":
    st.subheader("Create Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if email in st.session_state.users:
            st.error("User already exists")
        else:
            st.session_state.users[email] = {
                "name": name,
                "password": password
            }
            st.success("Registered Successfully!")

# ---------------- LOGIN ----------------
elif menu == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = st.session_state.users.get(email)

        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login Successful!")
        else:
            st.error("Invalid credentials")

# ---------------- BOOK APPOINTMENT ----------------
elif menu == "Book Appointment":
    if not st.session_state.get("logged_in"):
        st.warning("Please login first")
    else:
        st.subheader("Book Appointment")

        date = st.date_input("Select Date")
        time = st.time_input("Select Time")
        reason = st.text_area("Reason")

        if st.button("Book"):
            st.session_state.appointments.append({
                "email": st.session_state.user_email,
                "date": str(date),
                "time": str(time),
                "reason": reason
            })
            st.success("Appointment Booked!")

# ---------------- VIEW APPOINTMENTS ----------------
elif menu == "View Appointments":
    if not st.session_state.get("logged_in"):
        st.warning("Please login first")
    else:
        st.subheader("Your Appointments")

        for appt in st.session_state.appointments:
            if appt["email"] == st.session_state.user_email:
                st.write(f"📅 {appt['date']} ⏰ {appt['time']} - {appt['reason']}")
