from flask import Blueprint, request, jsonify, make_response
import json
from src import db

posts = Blueprint('Posts', __name__)

# delete a specific post

@posts.route('/deletepost/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM posts WHERE id = %s', (post_id,))
    db.get_db().commit()
    return 'Post {} has been deleted.'.format(post_id)


# post a new post

@posts.route('/postpost', methods=['POST'])
def create_post():
    # Get the data from the request
    data = request.get_json()

    # Insert the new post into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO posts (Genre_ID, Prompt_ID, Song_ID1, Song_ID2, Song_ID3, Song_ID4, User_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)',
               (data['Genre_ID'], data['Prompt_ID'], data['Song_ID1'], data['Song_ID2'], data['Song_ID3'], data['Song_ID4'], data['User_ID']))
    db.get_db().commit()

    # Return a response indicating that the post has been created
    return jsonify({'message': 'Post created successfully.'})


# update an existing post

@posts.route('/updatepost/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    # Get the data from the request
    data = request.get_json()

    # Update the post in the database
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE posts SET Genre_ID = %s, Prompt_ID = %s, Song_ID1 = %s, Song_ID2 = %s, Song_ID3 = %s, Song_ID4 = %s, User_ID = %s WHERE Post_ID = %s',
               (data['Genre_ID'], data['Prompt_ID'], data['Song_ID1'], data['Song_ID2'], data['Song_ID3'], data['Song_ID4'], data['User_ID'], post_id))
    db.get_db().commit()

    # Return a response indicating that the post has been updated
    return jsonify({'message': 'Post updated successfully.'})