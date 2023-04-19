from flask import Blueprint, request, jsonify, make_response
import json
from src import db


artists = Blueprint('artists', __name__)

@artists.route('/')
def home():
    return ('<h1>Hello from your artist page!!</h1>')

# Get all artists from the DB
@artists.route('/artists', methods=['GET'])
def get_artists():
    cursor = db.get_db().cursor()
    cursor.execute('select Artist_id, Name from Artist')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

query_song_eng = '''SELECT listens, views FROM SongEngagement 
                        WHERE Song_ID = {}; '''

# Get song engagement
@artists.route('/songeng<int:songid>', methods=['GET'])
def get_artists():
    cursor = db.get_db().cursor()
    cursor.execute(query_song_eng)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response