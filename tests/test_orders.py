from api import routes, models
''' 
This tests whether the 3Fs Menu collection is not empty
'''

def test_orders_available():
    models.orders = [{
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
    }]

    assert len(models.orders) == 1
