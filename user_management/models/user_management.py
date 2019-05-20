from mongoengine import *
import datetime

class loggedInUser(Document):
    email = StringField(max_length = 200, required = True)
    uid = StringField(max_length = 200, required = True, unique = True)
    timeOfRecentLogin = DateTimeField(default=datetime.datetime.now)

class User(Document):
    name = StringField(max_length = 200, required = True)
    email = StringField(max_length = 200, required = True)
    uid = StringField(max_length = 200, required = True, unique = True)
    timeCreated = DateTimeField(default=datetime.datetime.utcnow)

