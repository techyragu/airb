from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import initialize_routes
from database.db import initialize_db

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://admin:admin@my-mongodb.ygxbniv.mongodb.net/movie-bag'
}

initialize_db(app)
initialize_routes(api)


app.run()
