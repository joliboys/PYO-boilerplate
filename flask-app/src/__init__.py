# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'pyo'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add a default route
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the PYO boilerplate app</h1>"

    # Import the various routes
    from src.views import views
    from src.users.users import users
    from src.artists.artists  import artists
    from src.curators.curators  import curators
    from src.comments.comments import Comments
    from src.posts.posts import posts
    from src.songs.songs import songs
    from src.likes.likes import Likes

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(views,       url_prefix='/v')
    app.register_blueprint(users,       url_prefix='/u')
    app.register_blueprint(artists,     url_prefix='/a')
    app.register_blueprint(curators,    url_prefix='/c')
    app.register_blueprint(Comments,    url_prefix='/com')
    app.register_blueprint(posts,       url_prefix='/p')
    app.register_blueprint(songs,       url_prefix='/s')
    app.register_blueprint(Likes,       url_prefix='/l')

    return app
