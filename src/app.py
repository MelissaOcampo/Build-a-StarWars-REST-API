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
from models import db, Usuario, Personajes, Vehiculos, Planetas, Favoritos
#from models import Person

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

# Comienzan las rutas
@app.route('/personajes', methods=['GET'])
def get_personajes():
    all_personajes= Personajes.query.all()
    results = list(map(lambda item: item.serialize(),all_personajes))

    return jsonify(results), 200

@app.route('/personajes/<int:personajes_id>', methods=['GET'])
def select_personajes(personajes_id):
    personaje = Personajes.query.filter_by(id=personajes_id).first()
    return jsonify(personajes_id), 200

@app.route('/planetas', methods=['GET'])
def get_planetas():
    all_planetas= Planetas.query.all()
    results = list(map(lambda item: item.serialize(),all_planetas))
    return jsonify(results), 200

@app.route('/planetas/<int:planetas_id>', methods=['GET'])
def select_planetas(planetas_id):
    planetas = Planetas.query.filter_by(id=planetas_id).first()
    return jsonify(planetas_id), 200  

@app.route('/favoritos', methods=['GET'])
def get_favoritos():
    all_favoritos= Favoritos.query.all()
    results = list(map(lambda item: item.serialize(),all_favoritos))
    return jsonify(favoritos), 200


# Finalizan las rutas

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
