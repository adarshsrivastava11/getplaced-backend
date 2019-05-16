from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin

app = Sanic()
CORS(app)

@app.route("/login/")
async def test(request):
    return json({"res": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
