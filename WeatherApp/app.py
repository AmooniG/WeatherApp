from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import the CORS library
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS on the Flask app

API_KEY = '8892beb087a2d7acd8168d0b8304465c'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'Missing city parameter'}), 400
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.ok:
        data = response.json()
        print(data)  # Print the data to the console for debugging
        return jsonify(data)
    else:
        print(f"Error fetching weather data: {response.status_code} {response.text}")
        return jsonify({'error': 'Could not retrieve weather data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
