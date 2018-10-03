from flask import Flask
from flask_restful import Api

"""
Create a Flask application, named fff. 
fff short for fast-food-fast will be our flask instianted variable.
"""

fff = Flask(__name__)

from api import routes