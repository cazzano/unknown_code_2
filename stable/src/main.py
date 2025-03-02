# main.py
from flask import Flask
from create_db import initialize_databases
from routes import setup_routes

app = Flask(__name__)

# Initialize the databases when the app starts
initialize_databases()

# Set up the routes
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
