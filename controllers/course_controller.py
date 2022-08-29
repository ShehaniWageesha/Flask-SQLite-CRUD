from db import get_db
from flask import Flask, jsonify, make_response

app = Flask(__name__)

def insert_course(name, fee):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM course WHERE name = ?"
    cursor.execute(statement, [name])
    data = cursor.fetchall()
    if len(data) > 0:
        return make_response(jsonify({"message": "Course already exists", "user": {"name": name}, "error": "1", "meta": None}), 409)
    statement = "INSERT INTO course (name, fee) VALUES (?, ?)"
    cursor.execute(statement, [name, fee])
    db.commit()
    return make_response(jsonify({"message": "Course successfully created", "data": name, "error": "0", "meta": None}), 200)
