"""
This module provides functionality for gitHub workflows.

This is only a test program to simulate a deployment of a python app.

Author: Miguel Bustamante
Date: 11/06/2023
"""


from flask import Flask

app = Flask(__name__)
port = 3000


@app.route("/")
def hello_world():
    """Return 'Hello World' as a string."""
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    """Run the app in the port 3000 """
    app.run(port=port)
