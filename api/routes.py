from flask import jsonify, request
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
    ''' Function menu returns a list of available menu at 3fs '''
    return jsonify({'menu': models.menu})


@fff.route('/api/v1/client/orders/<string:username>', methods=['GET'])
def get_client_orders(username):
    ''' Function get_client_orders returns a list of 
    latest orders placed by a client'''
    client_orders = [order for order in models.orders \
    if order['clientName'].lower() == username.lower()]
    return jsonify({'latestOrders': client_orders})


@fff.route('/api/v1/orders', methods=['GET'])
def get_orders():
    ''' Function get_orders returns a list a of all orders '''
    return jsonify({'orders': models.orders})


@fff.route('/api/v1/orders', methods=['GET', 'POST'])
def place_order():
    """ Function place_order helps the client to place new order
    and also returns a list of all updated orders """
    mydata = request.get_json()
    new_order = {
        'orderID': mydata['orderID'],
        'orderStatus': mydata['orderStatus'],
        'orderDetails': mydata['orderDetails'],
        'orderQuantity': mydata['orderQuantity'],
        'orderFees': mydata['orderFees'],
        'clientName': mydata['clientName'],
        'clientNumber': mydata['clientNumber'],
        'clientAddress': mydata['clientAddress'],
        'assignedDriver': mydata['assignedDriver'],
        'approvalStatus': mydata['approvalStatus'],
        'orderRemarks': mydata['orderRemarks']
    }

    models.orders.append(new_order)
    return jsonify({'orders': models.orders})


@fff.route('/api/v1/orders/<int:id>', methods=['GET'])
@fff.route('/api/v1/client/orders/<int:id>', methods=['GET'])
def get_order_by_id(id):
    """ Function get_order_by_id returns a specific order """
    order_by_id = [order for order in models.orders \
    if order['orderID'] == id]
    return jsonify({'order': order_by_id})



