# Import dependencies
from flask import Flask

# Create a new Flask app instance
app = Flask(__name__)

# Create Flask Routes

# Define the Root first (ie the starting point)
@app.route('/')
def hello_world():
    return 'Hello world'
