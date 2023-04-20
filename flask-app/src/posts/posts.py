from flask import Blueprint, request, jsonify, make_response
import json
from src import db

posts = Blueprint('Posts', __name__)

# delete a specific post

@posts.route('/deletepost/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Posts WHERE id = %s', (post_id,))
    db.get_db().commit()
    return 'Post {} has been deleted.'.format(post_id)


# post a new post

@posts.route('/postpost', methods=['POST'])
def create_post():
    # Get the data from the request
    data = request.get_json()

    # Insert the new post into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Posts (Genre_ID, Prompt_ID, Song_ID1, Song_ID2, Song_ID3, Song_ID4, User_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)',
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
    cursor.execute('UPDATE Posts SET Genre_ID = %s, Prompt_ID = %s, Song_ID1 = %s, Song_ID2 = %s, Song_ID3 = %s, Song_ID4 = %s, User_ID = %s WHERE Post_ID = %s',
               (data['Genre_ID'], data['Prompt_ID'], data['Song_ID1'], data['Song_ID2'], data['Song_ID3'], data['Song_ID4'], data['User_ID'], post_id))
    db.get_db().commit()

    # Return a response indicating that the post has been updated
    return jsonify({'message': 'Post updated successfully.'})

# delete a specific comment

@posts.route('/delcomment/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM comments WHERE id = %s', (comment_id,))
    db.get_db().commit()
    return 'comment {} has been deleted.'.format(comment_id)


# post a new comment

@posts.route('/postcomment', methods=['POST'])
def create_comment():
    # Get the data from the request
    data = request.get_json()

    # Insert the new comment into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Comments (Comment, User_ID, Post_ID) VALUES (%s, %s, %s)',
               (data['Comment'], data['User_ID'], data['Post_ID']))
    db.get_db().commit()

    # Return a response indicating that the comment has been created
    return jsonify({'message': 'Comment created successfully.'})


# update an existing post

@posts.route('/updatecomment/<int:post_id>', methods=['PUT'])
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


# Get all liked posts
@posts.route('/getlikedposts<int:user_id>', methods=['GET'])
def get_liked_posts(user_id):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT Post_ID FROM Likes WHERE Likes.User_ID = {}".format(user_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response