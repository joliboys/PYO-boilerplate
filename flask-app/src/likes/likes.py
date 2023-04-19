from flask import Blueprint, request, jsonify, make_response
import json
from src import db


Likes = Blueprint('likes', __name__, url_prefix='/likes')

query_get_songs = '''SELECT Songs.Song_ID 
                     FROM Likes 
                     JOIN Posts ON Likes.Post_ID = Posts.Post_ID 
                     JOIN Songs ON (Songs.Song_ID = Posts.Song_ID 
                                OR Songs.Song_ID = Posts.Song_ID2 
                                OR Songs.Song_ID = Posts.Song_ID3 
                                OR Songs.Song_ID = Posts.Song_ID4) 
                     WHERE Likes.User_ID = {};'''

# Get all songs from liked posts
@Likes.route('/<int:user_id>', methods=['GET'])
def get_users(user_id):
    cursor = db.get_db().cursor()
    cursor.execute(query_get_songs.format(user_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
