from flask import *
from flask_restful import *
import pymysql
import json

app = Flask(__name__)
api = Api(app)

db_connection = pymysql.connect(
    host="localhost",
    user="root",
    database="medical_checker",
    passwd=""
)

@app.route('/')
def main():
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * from disease")
    row_headers = [x[0] for x in db_cursor.description]
    obj = {}
    data = []
    result = db_cursor.fetchall()
    for row in result:
        obj = {description: row[col] for col, description in enumerate(row_headers)}
        data.append(obj)
    return jsonify(data)

@app.route('/checkup')
def checkup():
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * from enquiry")
    row_headers = [x[0] for x in db_cursor.description]
    obj = {}
    data = []
    result = db_cursor.fetchall()
    for row in result:
        obj = {description: row[col] for col, description in enumerate(row_headers)}
        data.append(obj)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port='1234', debug=True)