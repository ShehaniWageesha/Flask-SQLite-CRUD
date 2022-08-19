from db import get_db
import bcrypt as bcrypt
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# user creation
def insert_user(nic, phone, password, qrcode, lastlogin):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM user WHERE nic = ?"
    cursor.execute(statement, [nic])
    data = cursor.fetchall()
    if len(data) > 0:
        return make_response(jsonify({"message": "User already exists", "user": {"nic": nic}, "error": "1", "meta": None}), 409)
    statement = "INSERT INTO user (nic, phone, password, qrcode, status, lastlogin) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [nic, phone, password, qrcode, '0', lastlogin])
    db.commit()
    return make_response(jsonify({"message": "User successfully created", "data": nic, "error": "0", "meta": None}), 200)


# user verify
def user_verify(nic, message):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT nic FROM user WHERE nic = ? AND qrcode = ? AND status = 0"
    cursor.execute(statement, [nic, message])
    result = [item[0] for item in cursor.fetchall()]
    x = len(result)
    if (x == 0):
        return make_response(jsonify({"message": "No records found", "data": None, "error": "1", "meta": None}), 404)
    if (x > 1):
        return make_response(jsonify({"message": "Multiple records found", "data": None, "error": "2", "meta": None}), 401)
    nic = result[0]
    statement = "UPDATE user SET status = '1' WHERE nic = ? AND qrcode = ? AND status = 0"
    cursor.execute(statement, [nic, message])
    db.commit()
    db.close()
    return make_response(jsonify({"message": "User verified successfully", "user": {"nic": nic}, "error": "0", "meta": None}), 200)


# user login
def login(nic, pw):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT nic, status, password FROM user WHERE nic = ? AND status = 1"
    cursor.execute(statement, [nic])
    result = cursor.fetchall()
    x = len(result)
    if (x == 0):
        return make_response(jsonify({"message": "No records found", "data": None, "error": "1", "meta": None}), 404)
    elif (x > 1):
        return make_response(jsonify({"message": "Multiple records found", "data": None, "error": "1", "meta": None}), 401)
    db_pw = ""
    for row in result:
        db_pw = row[2]
    compare_pw = bcrypt.checkpw(pw.encode('utf-8'), db_pw)
    if (compare_pw):
        return make_response(jsonify({"message": "User successfully logged-in.", "data": {"nic": nic}, "error": "0", "meta": None}), 200)
    return make_response(jsonify({"message": "Please check your credentials", "data": None, "error": "1", "meta": None}), 401)


# view user
def view_user(nic):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM user WHERE nic = ?"
    cursor.execute(statement, [nic])
    result = cursor.fetchall()
    x = len(result)
    if (x == 0):
        return make_response(jsonify({"message": "No records found", "data": None, "error": "1", "meta": None}), 404)
    elif (x > 1):
        return make_response(jsonify({"message": "Multiple records found", "data": None, "error": "1", "meta": None}), 401)
    return make_response(jsonify({"message": "User successfully retrieved", "data": str(result), "error": "0", "meta": None}), 200)

