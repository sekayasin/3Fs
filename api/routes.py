from flask import jsonify
from api import fff, models

@fff.route('/')
def index():
    ''' 
    This is the home page for our Fast-food-fast API
    This home page will consists of our API Documentation
    '''
    return ''' 
    <html>
        <head>
            <title>Home - 3Fs API</title>
        </head>
        <body>
            <h1>3Fs API</h1>
            <p>Welcome to 3Fs API documentation home page.</p>
        </body>
    </html>
    '''

@fff.route('/api/v1/client/menu', methods=['GET'])
def menu():
    return jsonify({'menu': models.menu})

@fff.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': models.orders})