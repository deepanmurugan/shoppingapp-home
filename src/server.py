from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    ip_address = flask.request.remote_addr
    return "Requester IP: " + ip_address
