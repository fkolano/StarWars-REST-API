"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorite_Planets, Favorite_Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_users():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/user/favorites', methods=['GET'])
def get_all_favorites():

    response_body = {
        "msg": "Hello, this is your GET /user/favorites response "
    }

    return jsonify(response_body), 200

# @app.route('/user/<int:user_id>/favorites', methods=['POST'])
# def get_user_favorites(user_id):

#     response_body = {
#         "msg": "Hello, this is your GET /user/favorites response "
#     }

#     return jsonify(response_body), 200



@app.route('/characters', methods=['GET'])
def handle_characters():

    characters = Characters.query.all()
    all_characters = list(map(lambda character: character.serialize(), characters))
    return jsonify(all_characters), 200



@app.route('/characters/<int:id>', methods=['GET'])
def get_characters_characters(id):
    single_person = Characters.query.get(id)
    return jsonify(single_person.serialize()), 200


@app.route('/planets', methods=['GET'])
def handle_planets():
    planets = Planets.query.all()
    all_planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(all_planets), 200



@app.route('/planets/<int:id>', methods=['GET'])
def get_single_planets(id):
    single_person = Planets.query.get(id)
    return jsonify(single_person.serialize()), 200

@app.route('/favorite/characters/<int:id>', methods=['POST'])
def get_characters(id):
    single_person = Characters.query.get(id)
    return jsonify(single_person.serialize()), 200


@app.route('/favorite/planets/<int:id>', methods=['DELETE'])
def get_favorite_planets(id):
    single_person = Planets.query.get(id)
    return jsonify(single_person.serialize()), 200

@app.route('/favorite/characters/<int:id>', methods=['DELETE'])
def get_favorite_characters(id):
    single_person = Characters.query.get(id)
    return jsonify(single_person.serialize()), 200


    
# @app.route('/characters', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
