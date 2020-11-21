from flask import Flask
app = Flask(__name__)

@app.route("/service1")
def hello():
    return flask.request.host
