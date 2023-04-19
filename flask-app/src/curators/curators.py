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


@curators.route('/posteng', methods=['GET'])
def get_eng():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for the list of interactions
    cursor.execute('SELECT Views, Interactions FROM PostEngagement')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)