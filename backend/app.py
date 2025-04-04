from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import roast_user
import os

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "https://your-netlify-app.netlify.app",  # Add your Netlify domain
        ]
    }
})

@app.route('/roast', methods=['POST'])
def get_roast():
    data = request.json
    name = data.get('name')
    comeback = data.get('comeback')
    level = data.get('level')
    
    result = roast_user(name, comeback, level)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 