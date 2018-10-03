from flask import jsonify, request, render_template, url_for
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from api import fff, models, status, fastfoodfast_db

""" Setup the Flask-JWT-Extended extension """
fff.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(fff)

menu = models.Menu()
order = models.Orders()
db = fastfoodfast_db.DatabaseConnection()

""" error handler 405, 404, 500 """
@fff.errorhandler(405)
def url_not_found(error):
    return jsonify({'message':'Requested method not allowed'}), status.HTTP_405_METHOD_NOT_ALLOWED

@fff.errorhandler(404)
def page_not_found(error):
    return jsonify({'message':'page not found, check the url'}), status.HTTP_404_NOT_FOUND

@fff.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error'}), status.HTTP_500_INTERNAL_SERVER_ERROR

@fff.route('/')
def index():
    ''' 
    This is the home page for our Fast-food-fast API
    home page which consists of our API Documentation
    '''
    return render_template('index.html')

@fff.route('/auth/signup', methods=['POST'])
def signup():
    """ Register a new user """
    
    firstname = request.json.get('first_name', None)
    lastname = request.json.get('last_name', None)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    address = request.json.get('email', None)
    tel = request.json.get('tel', None)

    if not firstname:
        return jsonify({"msg": "Missing first_name parameter"}), status.HTTP_400_BAD_REQUEST
    if not lastname:
        return jsonify({"msg": "Missing last_name parameter"}), status.HTTP_400_BAD_REQUEST
    if not username:
        return jsonify({"msg": "Missing username parameter"}), status.HTTP_400_BAD_REQUEST
    if not password:
        return jsonify({"msg": "Missing password parameter"}), status.HTTP_400_BAD_REQUEST
    if not email:
        return jsonify({"msg": "Missing email parameter"}), status.HTTP_400_BAD_REQUEST
    if not address:
        return jsonify({"msg": "Missing address parameter"}), status.HTTP_400_BAD_REQUEST
    if not tel:
        return jsonify({"msg": "Missing tel parameter"}), status.HTTP_400_BAD_REQUEST 

    parsejson = request.get_json()
    firstname = parsejson['first_name']
    lastname = parsejson['last_name']
    username = parsejson['username']
    password = parsejson['password']
    email = parsejson['email']
    address = parsejson['address']
    tel = parsejson['tel']
    if firstname and lastname and username and password and password and email and address and tel:
        db.user_sign_up(firstname, lastname, username, password, email, address, tel)
        return jsonify({
            'message': 'Hi {}!, You have successful created an account on fast-food-fast'.format(username)
            }), status.HTTP_200_OK
    

"""
Provide a method to create access tokens. The create_access_token()
function is used to actually generate the token, and you can return
it to the caller however you choose
"""
@fff.route('/auth/login', methods=['POST'])
def signin():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), status.HTTP_400_BAD_REQUEST
    if not password:
        return jsonify({"msg": "Missing password parameter"}), status.HTTP_400_BAD_REQUEST
    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), status.HTTP_401_UNAUTHORIZED

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), status.HTTP_200_OK

# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@fff.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200




