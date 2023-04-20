from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

posts = Blueprint('Posts', __name__)

@posts.route('/')
def home():
    return ('<h1>Hello from your posts page!!</h1>')

# Get all users from the DB

@posts.route('/posts', methods=['GET'])
def get_posts():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Posts')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# delete a specific post

@posts.route('/deletepost<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Posts WHERE Post_ID = %s', (post_id,))
    db.get_db().commit()
    return 'Post {} has been deleted.'.format(post_id)

# create a new post

@posts.route('/createpost', methods=['POST'])
def create_post():
    # Get the data from the request
    data = request.get_json()
    current_app.logger.info(data)

    # Insert the new post into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Posts (Genre_ID, Prompt_ID, Song_ID, Song_ID2, Song_ID3, Song_ID4, User_ID, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                   (data['Genre_ID'], data['Prompt_ID'], data['Song_ID'], data['Song_ID2'], data['Song_ID3'], data['Song_ID4'], data['User_ID'], data['timestamp']))
    db.get_db().commit()
    # Return a response indicating that the post has been created
    return jsonify({'message': 'Post created successfully.'})



# update an existing post

@posts.route('/updatepost', methods=['PUT'])
def update_post():
    # Get the data from the request
    data = request.get_json()
    # Update the post in the database
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Posts SET Genre_ID = %s, Prompt_ID = %s, Song_ID = %s, Song_ID2 = %s, Song_ID3 = %s, Song_ID4 = %s, User_ID = %s WHERE Post_ID = %s',
               (data['Genre_ID'], data['Prompt_ID'], data['Song_ID'], data['Song_ID2'], data['Song_ID3'], data['Song_ID4'], data['User_ID'], data['Post_ID']))
    db.get_db().commit()
    # Return a response indicating that the post has been updated
    return jsonify({'message': 'Post updated successfully.'})

# delete a specific comment

@posts.route('/delcomment<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Comments WHERE Comment_ID = %s', (comment_id,))
    db.get_db().commit()
    return 'comment {} has been deleted.'.format(comment_id)

# post a new comment

@posts.route('/postcomment', methods=['POST'])
def create_comment():
    # Get the data from the request
    data = request.get_json()
    # Insert the new comment into the database
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Comments (Comment, User_ID) VALUES (%s, %s)',
               (data['Comment'], data['User_ID']))
    db.get_db().commit()
    # Return a response indicating that the post has been created
    return jsonify({'message': 'Post created successfully.'})

# update an existing comment

@posts.route('/updatecomment', methods=['PUT'])
def update_comment():
    # Get the data from the request
    data = request.get_json()
    # Update the post in the database
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Comments SET Comment = %s WHERE Comment_ID = %s',
               (data['Comment'], data['Comment_ID']))
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

@posts.route('/genres', methods=['GET'])
def get_genre():
    cursor = db.get_db().cursor()
    cursor.execute('select distinct name, Genre_ID from Genre')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@posts.route('/songs', methods=['GET'])
def get_songs():
    cursor = db.get_db().cursor()
    cursor.execute('select distinct name, Song_ID from Songs')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@posts.route('/prompts', methods=['GET'])
def get_prompts():
    cursor = db.get_db().cursor()
    cursor.execute('select distinct * from Prompts')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
