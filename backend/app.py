from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

LOG_FILE = 'colors.json'

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as file:
        json.dump([], file)

# Get color log
@app.route('/api/colors', methods=['GET'])
def get_colors():
    try:
        with open(LOG_FILE, 'r') as file:
            colors = json.load(file)  # Attempt to load JSON
        return jsonify(colors)  # Return loaded colors as JSON
    except json.JSONDecodeError:
        # If the file is invalid JSON, reinitialize it
        with open(LOG_FILE, 'w') as file:
            json.dump([], file)
        return jsonify([])  # Return an empty list


# Add a color to the log
@app.route('/api/colors', methods=['POST'])
def add_color():
    try:
        # Extract color from the request payload
        data = request.json
        new_color = data.get('color')  # Get 'color' from the JSON payload

        if not new_color:
            return jsonify({'error': 'No color provided'}), 400

        with open(LOG_FILE, 'r') as file:
            colors = json.load(file)  # Load existing colors

        # Add the new color
        colors.append(new_color)

        with open(LOG_FILE, 'w') as file:
            json.dump(colors, file, indent=4)  # Save updated colors

        return jsonify({'message': 'Color added successfully', 'colors': colors}), 201
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle missing or invalid files
        colors = [new_color]
        with open(LOG_FILE, 'w') as file:
            json.dump(colors, file, indent=4)
        return jsonify({'message': 'File reinitialized with new color', 'colors': colors}), 201


if __name__ == '__main__':
    app.run(debug=True)
