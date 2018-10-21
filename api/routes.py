from flask import jsonify, request, render_template, url_for, redirect
from flask_cors import CORS, cross_origin
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from flasgger import swag_from
from api import fff, status, fastfoodfast_db

""" Setup the Flask-JWT-Extended extension """
fff.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(fff)

db = fastfoodfast_db.DatabaseConnection()

"""Create databases """
db.create_all_db_schemas()

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
    """ Redirect this route to swagger apidocs """
    return redirect('/apidocs')

    
@fff.route('/auth/signup', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
@swag_from('./templates/signup.yml')
def signup():
    """ Register a new user """
    
    firstname = request.json.get('first_name', None)
    lastname = request.json.get('last_name', None)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    address = request.json.get('address', None)
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
            }), status.HTTP_201_CREATED
    

"""
Provide a method to create access tokens. The create_access_token()
function is used to actually generate the token, and you can return
it to the caller however you choose
"""
@fff.route('/auth/login', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
@swag_from('./templates/signin.yml')
def signin():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), status.HTTP_400_BAD_REQUEST
    if not password:
        return jsonify({"msg": "Missing password parameter"}), status.HTTP_400_BAD_REQUEST
    
    parsejson = request.get_json()
    username = parsejson['username']
    password = parsejson['password']

    user = db.check_user_pass(username)
    try:
        if username == user['username']:
            if password == user["password"]:
                """ Identity can be any data that is json serializable """ 
                access_token = create_access_token(identity=username)
                return jsonify(access_token=access_token), status.HTTP_200_OK
            return jsonify({"msg": "Invalid Password"})
    except TypeError:
        return jsonify({"msg": "Invalid Username"}) 


""" Admin add menu option """
@fff.route('/menu', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
@jwt_required
@swag_from('./templates/add_menu.yml')
def add_menu_option():
    """ Add menu option """
    current_user = get_jwt_identity()
    username = current_user
    admin_user = db.check_user_pass(username)
    if admin_user['role_id'] == 1:
        dishname = request.json.get('dish_name', None)
        dishprice = request.json.get('dish_price', None)
        dishtoppings = request.json.get('dish_toppings', None)

        if not dishname:
            return jsonify({"msg": "Missing dish_name parameter"}), status.HTTP_400_BAD_REQUEST
        if not dishprice:
            return jsonify({"msg": "Missing dish_price parameter"}), status.HTTP_400_BAD_REQUEST
        if not dishtoppings:
            return jsonify({"msg": "Missing dish_toppings parameter"}), status.HTTP_400_BAD_REQUEST
        
        parsejson = request.get_json()
        dishname = parsejson['dish_name']
        dishprice = parsejson['dish_price']
        dishtoppings = parsejson['dish_toppings']
        
        if dishname and dishprice and dishtoppings:
            db.add_menu(dishname, dishprice, dishtoppings)
            return jsonify({'msg': '{} has been added on the menu'.format(dishname)}), status.HTTP_201_CREATED
    return jsonify({'msg': 'Admin Access only'}), status.HTTP_401_UNAUTHORIZED


""" Get Available menu """
@fff.route('/menu', methods=['GET'])
@cross_origin()
@swag_from('./templates/get_menu.yml')
def get_menu():
    """ Function get_menu returns a list of available menu at 3fs """
    return jsonify({'menu': db.get_menu()}), status.HTTP_200_OK

""" Place an order """
@fff.route('/users/orders', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
@jwt_required
@swag_from('./templates/place_order.yml')
def place_order():
    """ Function place_order helps the client to place new order """
    current_user = get_jwt_identity()
    username = current_user

    user_access = db.check_user_pass(username)

    if user_access['role_id'] == 2:
        meal = request.json.get('dish_name', None)
        order_quantity = request.json.get('order_quantity', None)
        total_order_cost = request.json.get('total_order_cost', None)

        if not meal:
            return jsonify({"msg": "Missing dish_name parameter"}), status.HTTP_400_BAD_REQUEST
        if not order_quantity:
            return jsonify({"msg": "Missing order_quantity parameter"}), status.HTTP_400_BAD_REQUEST
        if not total_order_cost:
            return jsonify({"msg": "Missing total_order_cost parameter"}), status.HTTP_400_BAD_REQUEST

        parsejson = request.get_json()
        meal = parsejson['dish_name']
        order_quantity = parsejson['order_quantity']
        total_order_cost = parsejson['total_order_cost']
        
        return jsonify({'message': db.place_order(username, meal, order_quantity, total_order_cost)}), status.HTTP_201_CREATED
    return jsonify({'msg': 'Kindly create a user account and place again your order'}), status.HTTP_401_UNAUTHORIZED


""" Get Specfic User Order history """
@fff.route('/users/orders', methods=['GET'])
@cross_origin()
@jwt_required
@swag_from('./templates/get_user_order_history.yml')
def get_user_order_history():
    ''' Function get_user_order_history returns the order history of the user '''
    current_user = get_jwt_identity()
    username = current_user

    user_access = db.check_user_pass(username)

    if user_access['role_id'] == 2:
        return jsonify({'orders': db.get_user_specific_orders_by_username(username)}), status.HTTP_200_OK
    return jsonify({'msg': 'Only registered users allowed to access their orders'}), status.HTTP_401_UNAUTHORIZED


@fff.route('/orders', methods=['GET'])
@cross_origin()
@jwt_required
@swag_from('./templates/get_all_order.yml')
def get_orders():
    ''' Function get_orders returns a list a of all orders '''
    current_user = get_jwt_identity()
    username = current_user
    admin_user = db.check_user_pass(username)

    if admin_user['role_id'] == 1:
        return jsonify({'orders': db.get_all_orders()}), status.HTTP_200_OK
    return jsonify({'msg': 'Admin Access only'}), status.HTTP_401_UNAUTHORIZED


@fff.route('/orders/<int:id>', methods=['GET'])
@cross_origin()
@jwt_required
@swag_from('./templates/get_order_by_id.yml')
def get_order_by_id(id):
    """ Function get_order_by_id returns a specific order """
    current_user = get_jwt_identity()
    username = current_user
    admin_user = db.check_user_pass(username)

    if admin_user['role_id'] == 1:
        return jsonify({'order': db.get_order_by_id(id)}), status.HTTP_200_OK
    return jsonify({'msg': 'Admin Access only'}), status.HTTP_401_UNAUTHORIZED


@fff.route('/orders/<int:id>', methods=['PUT'])
@cross_origin(allow_headers=['Content-Type'])
@jwt_required
@swag_from('./templates/update_order.yml')
def update_order_status(id):
    """ Function update_order_status updates the status of the order """
    current_user = get_jwt_identity()
    username = current_user
    admin_user = db.check_user_pass(username)

    if admin_user['role_id'] == 1:
        order_status = request.json.get('order_status', None)

        if not order_status:
            return jsonify({"msg": "Missing order_status parameter"}), status.HTTP_400_BAD_REQUEST

        parsejson = request.get_json()
        order_status = parsejson['order_status']
        return jsonify({'order': db.update_order_status(id, order_status)}), status.HTTP_201_CREATED
    return jsonify({'msg': 'Admin Access only'}), status.HTTP_401_UNAUTHORIZED
    

@fff.route('/orders/<int:id>', methods=['DELETE'])
@cross_origin()
@jwt_required
@swag_from('./templates/delete_order.yml')
def remove_completed_order(id):
    """ Function remove_completed_order removes finished order """
    current_user = get_jwt_identity()
    username = current_user
    admin_user = db.check_user_pass(username)

    if admin_user['role_id'] == 1:
        return jsonify({'message': db.remove_completed_order(id)}), status.HTTP_200_OK
    return jsonify({'msg': 'Admin Access only'}), status.HTTP_401_UNAUTHORIZED

    