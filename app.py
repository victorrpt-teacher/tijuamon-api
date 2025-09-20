from flask import Flask, jsonify, request, render_template # Import Flask and related modules

app = Flask(__name__) # Create a Flask application instance

# Memory storage for items
tijuamones = [
    {"id": 1, "name": "Caguamon", "type": "Water", "level": 5, "hp": 30, "attack": 15, "defense": 10, "habilities": ["Bottle Thrower", "Smell Attack"]},
    {"id": 2, "name": "Choloko", "type": "Fire", "level": 7, "hp": 40, "attack": 12, "defense": 14, "habilities": ["Smoke", "Knife Thrower"]},
    {"id": 3, "name": "Canalin", "type": "Dirt", "level": 6, "hp": 35, "attack": 14, "defense": 12, "habilities": ["Poisoned Water Thrower", "Mud Attack"]},
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/tijuamones', methods=['GET'])
def get_tijuamones():
    return jsonify(tijuamones)

if __name__ == "__main__":
    app.run(debug=True)