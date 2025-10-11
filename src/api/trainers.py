# blueprints  (routes) per resource
from flask import Blueprint, jsonify
from src.models import Trainer, Tijuamon
from src.extensions import db   # Import the db instance

blueprint = Blueprint('trainers', __name__)

@blueprint.route('/', methods=['GET'])
def get_trainers():
    """Returns the full list of Trainers in JSON format."""
    trainers = Trainer.query.all()  # Example of using the db instance
    return jsonify([t.to_dict() for t in trainers])

@blueprint.route('/<int:id>', methods=['GET'])
def get_trainer(id):
    """Returns a single Trainer by ID in JSON format."""
    trainer = Trainer.query.get_or_404(id)  # Example of using the db instance
    return jsonify(trainer.to_dict())

@blueprint.route('/', methods=['POST'])
def create_trainer():
    """Creates a new Trainer. (Implementation omitted for brevity)"""
    return jsonify({"message": "Create Trainer endpoint"}), 201

@blueprint.route('/<int:id>', methods=['PUT'])
def update_trainer(id):
    """Updates an existing Trainer. (Implementation omitted for brevity)"""
    return jsonify({"message": f"Update Trainer {id} endpoint"})

@blueprint.route('/<int:id>', methods=['DELETE'])
def delete_trainer(id):
    """Deletes a Trainer. (Implementation omitted for brevity)"""
    return jsonify({"message": f"Delete Trainer {id} endpoint"})
