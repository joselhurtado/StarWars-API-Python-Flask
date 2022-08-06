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
from models import db, User, Planet, Character, Starship
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
def handle_hello(): 

    response = {
        "msg": "Jose Hurtado"
    }

    return jsonify(response)

#Planet Get and Post Methiod Request
@app.route('/planet', methods=['GET'])
def planet_get():
    planet = Planet.query.all()
    planet_list = []
    response = {"results":planet_list}
    for i in planet:
        planet_list.append(i.serialize())
    
    return jsonify(response)

@app.route('/planet', methods=['POST'])
def planet_post():
    payload_planet = request.get_json() #payload_planet is just the name - We could change it
    info_planet = Planet(name=payload_planet['name'], diameter=payload_planet['diameter'], image=payload_planet['image'], gravity=payload_planet['gravity']) #Planet DB info from class
    db.session.add(info_planet)
    db.session.commit()
    
    return jsonify(reponse)

#Character Get and Post Methiod Request
@app.route('/character', methods=['GET'])
def character_get():
    character = Character.query.all()
    response = []
    for i in character:
        response.append(i.serialize())
    
    return jsonify(response)

@app.route('/character', methods=['POST'])
def character_post():
    payload_character = request.get_json() #payload_character is just the name - We could change it
    info_character = Character(name=payload_character['name'], gender=payload_character['gender'], image=payload_character['image'], homeworld=payload_character['homeworld']) #Character DB info from class
    db.session.add(info_character)
    db.session.commit()
    
    return 'Character Succesfully Added'

#Starship Get and Post Methiod Request
@app.route('/starship', methods=['GET'])
def starship_get():
    starship = Starship.query.all()
    response = []
    for i in starship:
        response.append(i.serialize())
    
    return jsonify(response)

@app.route('/starship', methods=['POST'])
def starship_post():
    payload_starship = request.get_json() #payload_starship is just the name - We could change it
    info_starship = Starship(name=payload_starship['name'], model=payload_starship['model'], image=payload_starship['image'], length=payload_starship['length']) #Starship DB info from class
    db.session.add(info_starship)
    db.session.commit()
    
    return 'Starship Succesfully Added'

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
