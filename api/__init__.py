from flask import Flask

"""
Create a Flask application, named fff. 
fff short for fast-food-fast will be our flask instianted variable.
"""

fff = Flask(__name__)

from api import routes