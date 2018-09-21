''' 
This module contain our api data
At a moment, the data structures will be
used to store our data in memory
'''


''' 
The menu is a list of dishes and their 
price available for order by 3Fs customers
'''
menu = [
    {
        'name': 'Pilawo',
        'cost': '30K UGX'
    },
    {
        'name': 'Beef Luwombo',
        'cost': '50K UGX'
    },
    {
        'name': 'Chicken Luwombo',
        'cost': '100K UGX'
    },
    {
        'name': 'Goat Pilawo',
        'cost': '50K UGX'
    },
    {
        'name': 'Chicken Pilawo',
        'cost': '50K UGX'
    }
]

''' The orders of a list of orders made by 3Fs customers '''

orders = [
    {
        'orderID': 1,
        'orderStatus': 'Success',
        'orderDetails': 'Pilawo',
        'orderQuantity': 1,
        'orderFees': '30K UGX',
        'clientName': 'John Doe',
        'clientNumber': '0772 062954',
        'clientAddress': '12A Kevina Rd',
        'assignedDriver': 'Salongo Boda',
        'approvalStatus': 'Accpted',
        'orderRemarks': 'Completed'
    },
    {
        'orderID': 2,
        'orderStatus': 'Rejected',
        'orderDetails': 'Pilawo',
        'orderQuantity': 3,
        'orderFees': '60K UGX',
        'clientName': 'John Doe',
        'clientNumber': '0772 062954',
        'clientAddress': '12A Kevina Rd',
        'assignedDriver': 'Boltman Driver',
        'approvalStatus': 'Accpted',
        'orderRemarks': 'Pending'
    },
    {
        'orderID': 3,
        'orderStatus': 'Success',
        'orderDetails': 'Pilawo',
        'orderQuantity': 1,
        'orderFees': '30K UGX',
        'clientName': 'John Doe',
        'clientNumber': '0772 062954',
        'clientAddress': '12A Kevina Rd',
        'assignedDriver': 'Boltman Driver',
        'approvalStatus': 'Accpted',
        'orderRemarks': 'Completed'
    } 
]