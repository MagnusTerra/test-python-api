# Import the Flask library
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    # Return a simple HTML response
    return "<p>Hello, World!</p>"
