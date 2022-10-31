from flask import Flask, request
from flask_cors import CORS
from flask.json import jsonify


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {"msg" : "This api works!"}



if __name__ == '__main__':
    app.run(debug = True)