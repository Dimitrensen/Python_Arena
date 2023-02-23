import classes

def create_user:
  mock_user = classes.User("asjhdad","mucha@cz",classes.role.Admin)
  
  mock_user_details = classes.userDetails(
    name="Mia"
    body_type=classes.bodyType.lean,
    hair_color=classes.hairColor.Blond,
    personality_type=classes.personalityType.INTJ,
    hobbies=[classes.hobbies.Running, classes.hobbies.Hiking],
    zodiac=classes.zodiac.Leo,
    gender=classes.gender.Female,
    location=classes.location(longitude=45.5, latitude=34.2),
    description="I am have mean cooking skills and I am very patient."
  )

  mock_user_preferences = ?

   # create user preferences instance
    user_pref = classes.userPref(

# import <package> from  <library>
# import <library>

#(manually fix user details, preferences, etc. so when we do a print everything to be created)
# if you print the user class remember to use user.__dict__

