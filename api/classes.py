
class location:
	def __init__(self,longitude,latitude):
		self.latitude=latitude
		self.longitude=longitude



class personalityType:
	ESTJ=0
	ENTJ=1
	ESFJ=2
	ENFJ=3
	ISTJ=4
	ISFJ=5
	INTJ=6
	INFJ=7
	ESTP=8
	ESFP=9
	ENTP=10
	ENFP=11
	ISTP=12
	ISFP=13
	INTP=14
	INFP=15


class zodiac:
	Aries=1
	Taurus=2
	Gemini=3
	Cancer=4
	Leo=5
	Virgo=6
	Libra=7
	Scorpio=8
	Sagittarius=9
	Capricorn=10
	Aquarius=11
	Pisces=12


class bodyType:
	athletic=0
	chubby=1
	lean=2
	petite=3
	masculine=4


class hobbies:
	Football=0
	Yoga=1
	Games=2
	Cooking=3
	Running=4
	Dancing=5
	Hiking=6


class hairColor:
	Brunette=0
	Blond=1
	Black=2
	Red=3
	Blue=4


class gender:
	Female=0
	Male=1
	Other=2


class role:
	User="User"
	Admin="Admin"
	Superuser="Superuser"

class userDetails(object):
	def __init__(self,name,age,body_type,hair_color,personality_type,hobbies,zodiac,gender,location,description):
		self.name=name
		self.body_type=body_type
		self.hair_color=hair_color
		self.personality_type=personality_type
		self.hobbies=hobbies
		self.zodiac=zodiac
		self.gender=gender
		self.location=location
		self.description=description
		self.age=age


class User(object):
	def __init__(self,id,role,email,password):
		self.role=role
		self.email=email
		self.password=password
		self.Details=""
		self.Preferences=""
		self.username_generator()
		self.id=id

	def username_generator(self):
		self.username = self.email[:3] + self.role[:2]


class userPreferences(object):
	def __init__(self,age,body_type,hair_color,personality_type,hobbies,zodiac,gender,location):
		self.age=age
		self.body_type=body_type
		self.hair_color=hair_color
		self.personality_type=personality_type
		self.hobbies=hobbies
		self.zodiac=zodiac
		self.gender=gender
		self.location=location