from sanic import Sanic
from sanic import response
from sanic_cors import CORS, cross_origin
import datetime
import json 
import firebase_admin
from firebase_admin import credentials
import os

from mongoengine import connect


from models.user_management import loggedInUser

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../getplaced-backend.json')
cred = credentials.Certificate(filename)
default_app = firebase_admin.initialize_app(cred)

app = Sanic()
CORS(app)
connect("getPlacedTest")

@app.route("/login", methods=['POST'])
async def login(request):
    req = request.json
    res = 500
    msg = "Failed"
    logged_in_user = loggedInUser.objects(uid = req['uid'])
    if (logged_in_user):
        logged_in_user.update(timeOfRecentLogin = datetime.datetime.now)
        res = 200
        msg = "User Login Successful"
    else:
        logged_in_user = loggedInUser(req['email'], req['uid'])
        logged_in_user.save()
        res = 201
        msg = "User Login Successful"
    return response.json({"response": res, "message": msg})

@app.route("/logout", methods=['POST'])
async def logout(request):
    req = request.json
    res = 500
    msg = "Failed"
    logged_in_user = loggedInUser.objects(uid = req['uid'])
    if (logged_in_user):
        logged_in_user.delete()
        res = 200
        msg = "User Logged Out Successfully"
    else:
        res = 404
        msg = "User Not Logged In"
    return response.json({"response": res, "message": msg})

@app.route("/signup", methods=['POST'])
async def signup(request):
    req = request.json
    res = 500
    msg = "Failed"
    try:
        user = User(name = req['name'], email = req['email'], uid = req['uid'])
        user.save()
        res = 201
        msg = "User Created Successfully"
    except Exception as e:
        res = 200
        msg = "User Already Exists"
    return response.json({"response": res, "message": msg})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
