__author__ = "Gowtham"
__date__ = "4th Nov 2021"


from flask import Flask, send_from_directory
import os

root = os.path.dirname(os.path.realpath(__file__)) # Global root path definition to find the file locations/directories

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return send_from_directory(os.path.join(root,'templates'),'index.html')

@app.route('/tri')
def ri_tech():
    """Print 'Hello, world!' as the response body."""
    return '2nd page of Book Inventory'


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")