import classes

def create_user():
  mock_user = classes.User(classes.role.Admin,"mucha@cz",155678, )

#(manually fix user details, preferences, etc. so when we do a print everything to be created)
# if you print the user class remember to use user.__dict__
  
  mock_user_details = classes.userDetails(
    "Mia",
    25,
    classes.bodyType.lean,
    classes.hairColor.Blond,
    classes.personalityType.INTJ,
    [classes.hobbies.Running, classes.hobbies.Hiking],
    classes.zodiac.Leo,
    classes.gender.Female,
    classes.location(longitude=45.5, latitude=34.2),
    "I am have mean cooking skills and I am very patient."
  )

  user_preferences = classes.userPreferences(
    (23, 35),
    [classes.bodyType.chubby, classes.bodyType.athletic]
    [classes.hairColor.Blond, classes.hairColor.Red],
    classes.personalityType.ENFJ,
    [classes.hobbies.Running, classes.hobbies.Hiking],
    [classes.zodiac.Aries, classes.zodiac.Sagittarius],
    classes.gender.Male,
    classes.location(longitude=47.1, latitude=33.8)
    )
# import <package> from  <library>
# import <library>

  return mock_user

user = create_user()
print(user.__dict__)
