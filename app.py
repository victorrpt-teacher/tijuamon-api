from flask import Flask, jsonify, request, render_template # Import Flask and related modules
from models import Tijuamon # Import the Tijuamon model

app = Flask(__name__) # Create a Flask application instance


# Memory storage for items
tijuamones = [
    {"id": 1, "name": "Caguamon", "type": "Water", "level": 5, "hp": 30, "attack": 15, "defense": 10, "habilities": ["Bottle Thrower", "Smell Attack"]},
    {"id": 2, "name": "Choloko", "type": "Fire", "level": 7, "hp": 40, "attack": 12, "defense": 14, "habilities": ["Smoke", "Knife Thrower"]},
    {"id": 3, "name": "Canalin", "type": "Dirt", "level": 6, "hp": 35, "attack": 14, "defense": 12, "habilities": ["Poisoned Water Thrower", "Mud Attack"]},
    {"id": 4, "name": "BurroCebra", "type": "Normal", "level": 8, "hp": 45, "attack": 18, "defense": 11, "habilities": ["Tourist Trap", "Slow Attack"]},
    {"id": 5, "name": "Mimoy", "type": "Psych", "level": 10, "hp": 50, "attack": 20, "defense": 15, "habilities": ["Mind Control", "Hypnosis"]},
    {"id": 6, "name": "Maguana", "type": "Rock", "level": 12, "hp": 60, "attack": 25, "defense": 20, "habilities": ["Rock Throw", "Growl"]},
    {"id": 7, "name": "Policon", "type": "Electric", "level": 15, "hp": 70, "attack": 30, "defense": 25, "habilities": ["Bite", "Ticketing"]}
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/tijuamones', methods=['GET'])
def get_tijuamones():
    return jsonify(tijuamones)

if __name__ == "__main__":
    app.run(debug=True)