from flask import Flask, jsonify, request, render_template # Import Flask and related modules

app = Flask(__name__) # Create a Flask application instance

# Memory storage for items
tijuamones = [
    {"id": 1, "name": "Tijuamon A", "type": "Fire", "level": 5, "hp": 30, "attack": 15, "defense": 10, "habilities": ["Flame Thrower", "Quick Attack"]},
    {"id": 2, "name": "Tijuamon B", "type": "Water", "level": 7, "hp": 40, "attack": 12, "defense": 14, "habilities": ["Water Gun", "Bubble Beam"]},
    {"id": 3, "name": "Tijuamon C", "type": "Grass", "level": 6, "hp": 35, "attack": 14, "defense": 12, "habilities": ["Vine Whip", "Razor Leaf"]},
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/tijuamones', methods=['GET'])
def get_tijuamones():
    return jsonify(tijuamones)

if __name__ == "__main__":
    app.run(debug=True)