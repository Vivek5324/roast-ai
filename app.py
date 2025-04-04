from flask import Flask, render_template, request, jsonify
from chat import roast_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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