from flask import Flask, request, jsonify
from utils.db import users_collection, appointments_collection

app = Flask(__name__)

# ------------------ REGISTER ------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    users_collection.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    })

    return jsonify({"message": "User registered successfully"})


# ------------------ LOGIN ------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = users_collection.find_one({
        "email": data["email"],
        "password": data["password"]
    })

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# ------------------ BOOK APPOINTMENT ------------------
@app.route("/book", methods=["POST"])
def book():
    data = request.json

    # Check if slot already booked
    existing = appointments_collection.find_one({
        "date": data["date"],
        "time": data["time"]
    })

    if existing:
        return jsonify({"message": "Slot already booked"}), 400

    appointments_collection.insert_one({
        "name": data["name"],
        "date": data["date"],
        "time": data["time"]
    })

    return jsonify({"message": "Appointment booked successfully"})


# ------------------ VIEW APPOINTMENTS ------------------
@app.route("/appointments", methods=["GET"])
def get_appointments():
    appointments = list(appointments_collection.find({}, {"_id": 0}))
    return jsonify(appointments)


if __name__ == "__main__":
    app.run(debug=True)
