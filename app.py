import streamlit as st

st.set_page_config(page_title="Appointment Booking System", page_icon="📅")

# ---------------- SESSION STORAGE ----------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "appointments" not in st.session_state:
    st.session_state.appointments = []

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = None

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.selectbox(
    "Menu",
    ["Register", "Login", "Book Appointment", "View Appointments", "Logout"]
)

# ---------------- TITLE ----------------
st.title("📅 Appointment Booking System")

# ---------------- REGISTER ----------------
if menu == "Register":
    st.subheader("Create Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if not name or not email or not password:
            st.warning("Please fill all fields")
        elif email in st.session_state.users:
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
    if not st.session_state.logged_in:
        st.warning("Please login first")
    else:
        st.subheader("Book Appointment")

        date = st.date_input("Select Date")
        time = st.time_input("Select Time")
        reason = st.text_area("Reason")

        if st.button("Book Appointment"):
            if not reason:
                st.warning("Please enter a reason")
            else:
                st.session_state.appointments.append({
                    "email": st.session_state.user_email,
                    "date": str(date),
                    "time": str(time),
                    "reason": reason
                })
                st.success("Appointment Booked Successfully!")

# ---------------- VIEW APPOINTMENTS ----------------
elif menu == "View Appointments":
    if not st.session_state.logged_in:
        st.warning("Please login first")
    else:
        st.subheader("Your Appointments")

        found = False
        for appt in st.session_state.appointments:
            if appt["email"] == st.session_state.user_email:
                found = True
                st.write(f"📅 {appt['date']} ⏰ {appt['time']}")
                st.write(f"📝 {appt['reason']}")
                st.markdown("---")

        if not found:
            st.info("No appointments found")

# ---------------- LOGOUT ----------------
elif menu == "Logout":
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.success("Logged out successfully")
