from flask import Blueprint, request, jsonify, make_response
import json
from src import db


# delete a specific post

@posts.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM posts WHERE id = %s', (post_id,))
    db.get_db().commit()
    return 'Post {} has been deleted.'.format(post_id)

# post a new post

@posts.route('/posts', methods=['POST'])
def create_post():
    # Get the data from the request
    data = request.get_json()

    # Insert the new post into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO posts (title, content) VALUES (%s, %s)',
                   (data['title'], data['content']))
    db.get_db().commit()

    # Return a response indicating that the post has been created
    return jsonify({'message': 'Post created successfully.'})