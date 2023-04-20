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


# Get song engagement
@artists.route('/songeng<int:Song_ID>', methods=['GET'])
def get_songeng(Song_ID):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT listens, views 
                        FROM SongEngagement
                        WHERE Song_ID = %s''', (Song_ID))

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# add a new song

@artists.route('/addsong', methods=['POST'])
def create_song():
    # Get the data from the request
    data = request.get_json()

    # Insert the new song into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Songs (Song_ID, Genre_ID, Artist_ID, Name) VALUES (%s, %s, %s, %s)',
               (data['Song_ID'], data['Genre_ID'], data['Artist_ID'], data['Name']))
    db.get_db().commit()

    # Return a response indicating that the post has been created
    return jsonify({'message': 'Post created successfully.'})

# delete a song

@artists.route('/deletesong<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Delete the song from the database
    cursor.execute('DELETE FROM Songs WHERE Song_ID = %s', (song_id,))
    db.get_db().commit()

    # Return a response indicating that the song has been deleted
    return jsonify({'message': 'Song deleted successfully.'})

# get post engagement

@artists.route('/posteng<int:Post_ID>', methods=['GET'])
def get_eng(Post_ID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for the list of interactions
    cursor.execute("SELECT Views, Interactions FROM PostEngagement WHERE Post_ID = %s", (Post_ID))

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

# Get posts with their songs in it
@artists.route('/songposts<int:Song_ID>', methods=['GET'])
def get_songposts(Song_ID):
    cursor = db.get_db().cursor()
    query = '''SELECT Post_ID
                FROM Posts
                WHERE Song_ID IN (
                    SELECT Song_ID
                    FROM Songs
                    WHERE Song_ID = {}
                ) OR Song_ID2 IN (
                    SELECT Song_ID
                    FROM Songs
                    WHERE Song_ID = {}
                ) OR Song_ID3 IN (
                    SELECT Song_ID
                    FROM Songs
                    WHERE Song_ID = {}
                ) OR Song_ID4 IN (
                    SELECT Song_ID
                    FROM Songs
                    WHERE Song_ID = {})'''
    cursor.execute(query, (Song_ID))

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response