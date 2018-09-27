from datetime import datetime

''' 
This module contains our api data
At a moment, data structures will be
used to store our data in memory
'''

class Menu:

    def __init__(self):
        ''' 
        The menu instance variable is a list of dishes and their 
        price available for order by 3Fs customers at 3fs takeaway
        '''
        self.available_menu = []
    
    def add_menu(self, meal_course, price):
        self.meal_course = meal_course
        self.price = price
        self.available_menu.append({
            'name': self.meal_course,
            'price': self.price
        })
    
    def get_available_menu(self):
        return self.available_menu


class Orders:

    order_id = 0

    def __init__(self):
        ''' The orders of a list of orders made by 3Fs customers '''
        self.orders = []
        self.order_status = "pending"
    
    def add_order(self, order_details, order_quantity, order_fees, client_name, client_address):
        """ order_id will be automatically generated unpon placing an order """
        self.__class__.order_id += 1
        self.order_details = order_details
        self.order_quantity = order_quantity
        self.order_fees = order_fees
        self.client_name = client_name
        self.client_address = client_address
        self.order_date_timestamp = str(datetime.now())
        self.orders.append({
            'orderID': self.__class__.order_id,
            'orderDetails': self.order_details,
            'orderQuantity': self.order_quantity,
            'orderFees': self.order_fees,
            'clientName': self.client_name,
            'clientAddress': self.client_address,
            'orderStatus': self.order_status,
            'orderDate': self.order_date_timestamp
        })
    
    def get_orders(self):
        return self.orders

    def get_order_by_id(self, id):
        order_by_id = [order for order in self.orders if order['orderID'] == id]
        return order_by_id 
    
    def update_order_status(self, id, status_msg):
        order_to_change_status = [order for order in self.orders if order['orderID'] == id]
        order_to_change_status[0]['orderStatus'] = status_msg
        return order_to_change_status
    
    def remove_order(self, id):
        completed_order = [order for order in self.orders if order['orderID'] == id]
        self.orders.remove(completed_order[0])
        return self.orders
        
            
