from flask import Flask,request
import classes
import json
users = []

app = Flask(__name__)

@app.route("/users")
def get_all_users():
    array = []
    for user in users:
        array.append(user.__dict__)
    return array

@app.route("/user/create")
def create_user():
    id = len(users)
    data = request.get_json()
    role = data.get("role", "")
    email = data.get("email", "")
    password = data.get("password", 0)
    user = classes.User(id, role, email, password)
    users.append(user)
    return user.__dict__

@app.route("/details/user", methods=["POST"])
def create_user_details():
    data = request.get_json()
    name = data.get("name", "")
    body_type = data.get("body_type", 0)
    hair_color = data.get("hair_color", 0)
    personality_type = data.get("personality_type", 0)
    hobbies = data.get("hobbies", 0)
    zodiac = data.get("zodiac", 0)
    gender = data.get("gender", 0)
    location = data.get("location")
    description = data.get("description", "")
    age = data.get("age", 0)
    
    latitude=location["latitude"]
    longitude=location["longitude"]
    location_instance=classes.location


    return 'ok'

#find the user with this id, and get the data from the request and fill it in to the user
    # for user in users:
    #     if user.id == id:
    #         user.Details=details
    #         break
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
