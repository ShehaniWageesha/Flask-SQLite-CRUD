import sys

sys.dont_write_bytecode = True

from db import create_tables
from helper.id_generate import generate_pin
from helper.password import hashpw
import controllers.user_controller as user_controller
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime as dt

app = Flask(__name__)
CORS(app)

@app.route("/api/user", methods=["POST"])
def insert_user():
    user_details = request.get_json()
    nic = user_details["nic"]
    phone = user_details["phone"]
    password = user_details["password"]
    password = hashpw(password)
    qrcode = generate_pin(5)
    date = dt.datetime.now()
    result = user_controller.insert_user(
        nic, phone, password, qrcode, date)
    return result


@app.route('/api/user-verify', methods=["POST"])
def user_verify():
    nic = request.args.get('nic', None)
    message = request.args.get('message', None)
    result = user_controller.user_verify(nic, message)
    return result

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    nic = data['nic']
    pw = data['password']
    result = user_controller.login(nic, pw)
    return result


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    create_tables()
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
