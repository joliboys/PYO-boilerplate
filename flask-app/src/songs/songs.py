from flask import Blueprint, request, jsonify, make_response
import json
from src import db

songs = Blueprint('Songs', __name__)

# add a new song

@songs.route('/addsong', methods=['POST'])
def create_song():
    # Get the data from the request
    data = request.get_json()

    # Insert the new song into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Songs (Genre_ID, Artist_ID, Name) VALUES (%s, %s, %s)',
               (data['Genre_ID'], data['Artist_ID'], data['Name']))
    db.get_db().commit()

    # Return a response indicating that the post has been created
    return jsonify({'message': 'Post created successfully.'})
