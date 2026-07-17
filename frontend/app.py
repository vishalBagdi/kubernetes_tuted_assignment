from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

PORT = os.environ.get('PORT', 9000)
backend_url = os.environ.get('BACKEND_URL', 'http://localhost:8000')

@app.route('/')
def index():
    # Fetch data from the backend API
    response = requests.get(f'{backend_url}/api/get')
    data = response.json()
    print(data, type(data))

    env = dict(os.environ)
    

    return render_template('index.html', env=env, data=data['data'])
if __name__ == '__main__':
    app.run(debug=True, port=PORT, host='0.0.0.0')





