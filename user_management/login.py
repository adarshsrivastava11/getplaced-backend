from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('../getplaced-backend.json')
default_app = firebase_admin.initialize_app(cred)

app = Sanic()
CORS(app)

@app.route("/login/")
async def test(request):
    print (default_app)
    print (request.body)
    return json({"res": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
