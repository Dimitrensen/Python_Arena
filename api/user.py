import classes

def create_user:
  mock_user = classes.User("asjhdad","mucha@cz",classes.role.Admin)

#(manually fix user details, preferences, etc. so when we do a print everything to be created)
# if you print the user class remember to use user.__dict__
  
  mock_user_details = classes.userDetails(
    name="Mia"
    age=25
    body_type=classes.bodyType.lean,
    hair_color=classes.hairColor.Blond,
    personality_type=classes.personalityType.INTJ,
    hobbies=[classes.hobbies.Running, classes.hobbies.Hiking],
    zodiac=classes.zodiac.Leo,
    gender=classes.gender.Female,
    location=classes.location(longitude=45.5, latitude=34.2),
    description="I am have mean cooking skills and I am very patient."
  )

  user_pref = classes.userPref(
    preferred_age_range=(23, 35),
    preferred_body_type=[classes.bodyType.chubby, classes.bodyType.athletic]
    preferred_hair_color=[classes.hairColor.Blond, classes.hairColor.Red],
    preferred_personality_type=classes.personalityType.ENFJ,
    preferred_hobbies=[classes.hobbies.Running, classes.hobbies.Hiking],
    preferred_zodiac=[classes.zodiac.Aries, classes.zodiac.Sagittarius],
    preferred_gender=classes.gender.Male,
    preferred_location=classes.location(longitude=47.1, latitude=33.8)
    )
# import <package> from  <library>
# import <library>

return mock_user

user = create_user()
print(user.__dict__)
