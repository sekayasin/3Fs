from flask import jsonify, request, render_template, url_for
from api import fff, models, status

@fff.route('/')
def index():
    ''' 
    This is the home page for our Fast-food-fast API
    home page which consists of our API Documentation
    '''
    return render_template('index.html')

menu = models.Menu()
order = models.Orders()

@fff.route('/api/v1/menu', methods=['POST'])
def add_todays_menu():
    parsejson = request.get_json()
    meal = parsejson['name']
    price = parsejson['price']
    menu.add_menu(meal, price)
    return jsonify({'message': 'An item has been added on today\'s menu'}), status.HTTP_201_CREATED
    

@fff.route('/api/v1/client/menu', methods=['GET'])
def get_menu():
    ''' Function menu returns a list of available menu at 3fs '''
    return jsonify({'menu': menu.get_available_menu()}), status.HTTP_200_OK 


@fff.route('/api/v1/orders', methods=['POST'])
def place_order():
    """ Function place_order helps the client to place new order
    and also returns a list of all updated orders """
    parsejson = request.get_json()
    order_details = parsejson['orderDetails']
    order_quantity = parsejson['orderQuantity']
    order_fees = parsejson['orderFees']
    client_name = parsejson['clientName']
    client_address = parsejson['clientAddress']    
    order.add_order(order_details, int(order_quantity), order_fees, client_name, client_address)
    return jsonify({'message': 'You\'ve successfully placed an order, Your Request is forwarded to our master chef'}), status.HTTP_201_CREATED


@fff.route('/api/v1/orders', methods=['GET'])
def get_orders():
    ''' Function get_orders returns a list a of all orders '''
    return jsonify({'orders': order.get_orders()}), status.HTTP_200_OK


@fff.route('/api/v1/orders/<int:id>', methods=['GET'])
@fff.route('/api/v1/client/orders/<int:id>', methods=['GET'])
def get_order_by_id(id):
    """ Function get_order_by_id returns a specific order """
    return jsonify({'order': order.get_order_by_id(id)}), status.HTTP_200_OK


@fff.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_order_status(id):
    """ Function update_order_status updates the status of the order """
    parsejson = request.get_json()
    order_status = parsejson['orderStatus']
    return jsonify({'order': order.update_order_status(id, order_status)}), status.HTTP_201_CREATED


@fff.route('/api/v1/orders/<int:id>', methods=['DELETE'])
def remove_completed_order(id):
    """ Function remove_completed_order removes finished order """
    order.remove_order(id)
    return jsonify({'message': 'Successfully removed this completed order'}), status.HTTP_204_NO_CONTENT


# @fff.route('/api/v1/client/orders/<string:username>', methods=['GET'])
# def get_client_orders(username):
#     ''' Function get_client_orders returns a list of 
#     latest orders placed by a client'''
#     client_orders = [order for order in models.orders \
#     if order['clientName'].lower() == username.lower()]
#     return jsonify({'latestOrders': client_orders})




