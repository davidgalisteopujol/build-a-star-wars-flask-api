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
from models import db, User,Planet,People, fav_characters, fav_planets


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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


#Get all the users
@app.route('/users', methods=['GET'])
def handle_hello():
    all_users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users))
    response_body = all_users
    return jsonify(response_body),200
   

# Metodos para People
@app.route('/people', methods=['GET', 'POST'])
def handle_people():
    if request.method == 'POST':  
        body = request.get_json()
        character = People(
            name= body["name"],
            description = body["description"],
            height = body["height"]
        )
        db.session.add(character)
        db.session.commit()

        response_body = {
        "msg": "Hello, POST send"
        }
        return jsonify(response_body), 200
        
    if request.method=='GET':
        all_people = People.query.all()
        all_people = list(map(lambda x: x.serialize_people(), all_people))
        response_body = all_people
        return jsonify(response_body),200

#Detailed People
@app.route('/people/<int:id>', methods=['GET','PUT','DELETE'])
def handle_detailed_people(id):
    if request.method == 'GET':
        character = People.query.filter_by(id = id)
        character = list(map(lambda x: x.serialize_people(),character))
        response_body = character
        return jsonify(response_body),200
    
    if request.method == 'PUT':
        body = request.get_json()
        character = People.query.get(id)
        character.name = body["name"]
        character.description = body["description"]
        character.height = body["height"]
        db.session.commit()
        return jsonify(character.serialize_people()), 200

    if request.method == 'DELETE':
        character = People.query.get(id)
        db.session.delete(character)
        db.session.commit()
        return jsonify({"message":"character deleted"}),200
        

#Metodos para planet
@app.route('/planet', methods=['GET', 'POST'])
def handle_planet():
    if request.method == 'POST':
        body = request.get_json()
        new_planet = Planet(
            name= body["name"],
            description = body["description"],
            diameter = body["diameter"]
        )
        db.session.add(new_planet)
        db.session.commit()
        
        response_body = {
        "msg": "Hello, POST send"
        }

        return jsonify(response_body), 200
        
    if request.method=='GET':
        all_planet = Planet.query.all()
        all_planet = list(map(lambda x: x.serialize_planet(), all_planet))
        response_body = all_planet
        return jsonify(response_body),200


#Detailed Planet
@app.route('/planet/<int:id>',methods=['GET','PUT','DELETE'])
def handle_detailed_planet(id):
    if request.method == 'GET':
        detailed_planet = Planet.query.get(id)
        return jsonify(detailed_planet.serialize_planet(),200)

    if request.method == 'PUT':
        body = request.get_json()
        detailed_planet = Planet.query.get(id)
        detailed_planet.name = body["name"]
        detailed_planet.description = body["description"]
        detailed_planet.height = body["diameter"]
        db.session.commit()
        return jsonify(detailed_planet.serialize_planet()), 200

    if request.method == 'DELETE':
        planet = Planet.query.get(id)
        db.session.delete(planet)
        db.session.commit()
        return jsonify({"message":"planet deleted"}),200



#User Favorites
@app.route('/users/<int:user_id>/favorites')
def handle_favorites(user_id):
    user = User.query.get(user_id)

    favorites_characters = user.fav_characters
    favorites_characters = list(map(lambda x: x.serialize_people(), favorites_characters))

    favorites_planets = user.fav_planets
    favorites_planets = list(map(lambda x: x.serialize_planet(), favorites_planets))

    return jsonify(favorites_characters,favorites_planets),200


#Post favorite people in a user
@app.route('/user/<int:user_id>/favorites/people/<int:people_id>', methods=['POST'])
def handle_people_favorites(user_id,people_id):
    user = User.query.get(user_id)
    people = People.query.get(people_id)
    user.fav_characters.append(people)
    db.session.commit()

    response_body = {
    "msg": "Hello, POST send"
    }
    return jsonify(response_body), 200


#Post favorite planet in a user
@app.route('/user/<int:user_id>/favorites/planet/<int:planet_id>', methods=['POST'])
def handle_planet_favorites(user_id,planet_id):
    user = User.query.get(user_id)
    planet = Planet.query.get(planet_id)
    user.fav_planets.append(planet)
    db.session.commit()

    response_body = {
    "msg": "Hello, POST send"
    }
    return jsonify(response_body), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
