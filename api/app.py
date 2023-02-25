from flask import Flask,request
import classes
users = []

app = Flask(__name__)

@app.route("/users")
def get_all_users():
    return users

@app.route("/user/create")
def create_user():
    data = request.get_json()
    role = data.get("role", "")
    email = data.get("email", "")
    password = data.get("password", 0)
    user = classes.User(role, email, password)
    users.append(user)
    return user.__dict__