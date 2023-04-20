from flask import Blueprint, request, jsonify, make_response
import json
from src import db


curators = Blueprint('curators', __name__)

@curators.route('/')
def home():
    return ('<h1>Hello from your curator page!!</h1>')

# Get all curators from the DB
@curators.route('/curators', methods=['GET'])
def get_curators():
    cursor = db.get_db().cursor()
    cursor.execute('select Name, Curator_ID from Curator')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


