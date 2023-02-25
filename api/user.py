import classes

def create_user():
#(manually fix user details, preferences, etc. so when we do a print everything to be created)
# if you print the user class remember to use user.__dict__

  user_details = classes.userDetails(
    "Mia",
    25,
    classes.bodyType.lean,
    classes.hairColor.Blond,
    classes.personalityType.INTJ,
    [classes.hobbies.Running, classes.hobbies.Hiking],
    classes.zodiac.Leo,
    classes.gender.Female,
    classes.location(45.5, 34.2),
    "I am have mean cooking skills and I am very patient."
  )

  user_preferences = classes.userPreferences(
    [23, 35],
    [classes.bodyType.chubby, classes.bodyType.athletic],
    [classes.hairColor.Blond, classes.hairColor.Red],
    classes.personalityType.ENFJ,
    [classes.hobbies.Running, classes.hobbies.Hiking],
    [classes.zodiac.Aries, classes.zodiac.Sagittarius],
    classes.gender.Male,
    classes.location(47.1, 33.8)
    )
# import <package> from  <library>
# import <library>
  user = classes.User(classes.role.Admin,"mucha@banana.cz",155678 )
  user.Details=user_details
  user.Preferences=user_preferences
  return user

