from flask import Blueprint, request, jsonify, make_response
import json
from src import db

Comments = Blueprint('comments', __name__)

# delete a specific comment

@Comments.route('/delcomment/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM comments WHERE id = %s', (comment_id,))
    db.get_db().commit()
    return 'comment {} has been deleted.'.format(comment_id)


# post a new comment

@Comments.route('/postcomment', methods=['POST'])
def create_post():
    # Get the data from the request
    data = request.get_json()

    # Insert the new comment into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Comments (Comment, User_ID) VALUES (%s, %s)',
               (data['Comment'], data['User_ID']))
    db.get_db().commit()

    # Return a response indicating that the post has been created
    return jsonify({'message': 'Post created successfully.'})


# update an existing post

@Comments.route('/updatecomment/<int:post_id>', methods=['PUT'])
def update_comment(Comment_id):
    # Get the data from the request
    data = request.get_json()

    # Update the post in the database
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Comments SET Comment = %s, User_ID = %s WHERE Comment_ID = %s',
               (data['Comment'], data['User_ID'], Comment_id))
    db.get_db().commit()

    # Return a response indicating that the post has been updated
    return jsonify({'message': 'Post updated successfully.'})