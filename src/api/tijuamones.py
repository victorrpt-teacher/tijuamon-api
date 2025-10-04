# blueprints  (routes) per resource
from flask import Blueprint, jsonify
from src.models import Tijuamon

blueprint = Blueprint('tijuamones', __name__)

# Sample in-memory data
tijuamones: list[Tijuamon] = [
    Tijuamon(
        identifier=1,
        name="Caguamon",
        element_type="Water",
        level=5,
        hp=30,
        attack=15,
        defense=10,
        habilities=["Bottle Thrower", "Smell Attack"],
    ),
    Tijuamon(
        identifier=2,
        name="Choloko",
        element_type="Fire",
        level=7,
        hp=40,
        attack=12,
        defense=14,
        habilities=["Smoke", "Knife Thrower"],
    ),
    Tijuamon(
        identifier=3,
        name="Canalin",
        element_type="Dirt",
        level=6,
        hp=35,
        attack=14,
        defense=12,
        habilities=["Poisoned Water Thrower", "Mud Attack"],
    ),
    Tijuamon(
        identifier=4,
        name="BurroCebra",
        element_type="Normal",
        level=8,
        hp=45,
        attack=18,
        defense=11,
        habilities=["Tourist Trap", "Slow Attack"],
    ),
    Tijuamon(
        identifier=5,
        name="Mimoy",
        element_type="Psych",
        level=10,
        hp=50,
        attack=20,
        defense=15,
        habilities=["Mind Control", "Hypnosis"],
    ),
    Tijuamon(
        identifier=6,
        name="Maguana",
        element_type="Fire",
        level=9,
        hp=48,
        attack=22,
        defense=13,
        habilities=["Flame Tail", "Heat Wave"],
    ),
]

@blueprint.route('/', methods=['GET'])
def get_tijuamones():
    """Returns the full list of Tijuamon creatures in JSON format."""
    return jsonify([tijuamon.to_dict() for tijuamon in tijuamones])

@blueprint.route('/<int:identifier>', methods=['GET'])
def get_tijuamon(identifier: int):
    """Returns a specific Tijuamon by its identifier in JSON format."""
    tijuamon = next((t for t in tijuamones if t.identifier == identifier), None)
    if tijuamon:
        return jsonify(tijuamon.to_dict())
    return jsonify({"error": "Tijuamon not found"}), 404