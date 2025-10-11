# blueprints  (routes) per resource
from flask import Blueprint, jsonify
from src.models import Tijuamon
from src.extensions import db   # Import the db instance

blueprint = Blueprint('tijuamones', __name__)

@blueprint.route('/', methods=['GET'])
def get_tijuamones():
    """Returns the full list of Tijuamon creatures in JSON format."""
    tijuamones = Tijuamon.query.all()  # Example of using the db instance
    return jsonify([t.to_dict() for t in tijuamones])

@blueprint.route('/<int:id>', methods=['GET'])
def get_tijuamon(id):
    """Returns a single Tijuamon by ID in JSON format."""
    tijuamon = Tijuamon.query.get_or_404(id)  # Example of using the db instance
    return jsonify(tijuamon.to_dict())

@blueprint.route('/', methods=['POST'])
def create_tijuamon():
    """Creates a new Tijuamon. (Implementation omitted for brevity)"""
    return jsonify({"message": "Create Tijuamon endpoint"}), 201

@blueprint.route('/<int:id>', methods=['PUT'])
def update_tijuamon(id):
    """Updates an existing Tijuamon. (Implementation omitted for brevity)"""
    return jsonify({"message": f"Update Tijuamon {id} endpoint"})

@blueprint.route('/<int:id>', methods=['DELETE'])
def delete_tijuamon(id):
    """Deletes a Tijuamon. (Implementation omitted for brevity)"""
    return jsonify({"message": f"Delete Tijuamon {id} endpoint"})
