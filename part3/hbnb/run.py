#!/usr/bin/python3
from app import create_app
from flask_cors import CORS

app = create_app()
CORS(app)
app.config['PREFERRED_URL_SCHEME'] = 'http'

if __name__ == '__main__':
    app.run(debug=True)
