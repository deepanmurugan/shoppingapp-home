from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from service-1 by ABI"
