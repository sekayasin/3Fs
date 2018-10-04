from flask import Flask
from flasgger import Swagger

"""
Create a Flask application, named fff. 
fff short for fast-food-fast will be our flask instianted variable.
"""
fff = Flask(__name__)

""" Add swagger API Documentation """
Swagger(fff)

from api import routes