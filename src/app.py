"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Metodo creado por la academia


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members
    return jsonify(response_body), 200

# metodo GET


@app.route('/members/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "member not found"}), 404

# metodo Post


@app.route('/members', methods=['POST'])
def add_member():
    member_data = request.get_json()
    if not member_data or "first_name" not in member_data or "age" not in member_data or "lucky_numbers" not in member_data:
        return jsonify({"error": "invalido"}), 400
    
    jackson_family.add_member(member_data)
    return jsonify(member_data), 200


# metodo DELET
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if deleted:
        return jsonify({"done": True}), 200
    return jsonify({"error": "miembro no encontrado"}), 404


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
