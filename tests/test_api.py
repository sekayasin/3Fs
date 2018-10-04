import pytest
from datetime import datetime
from flask import Response, json
from api import fff, routes, models, status


def test_index():
    client = fff.test_client()
    res = client.get('/')
    assert res.status_code == status.HTTP_200_OK

def test_add_todays_menu():
    client = fff.test_client()
    res = client.post('/menu', json={'dish_name': 'Kikomando', 'price': 30, 'dish_toppings': 'milk'})
    assert res.status_code == status.HTTP_201_CREATED

def test_get_menu():
    client = fff.test_client()
    res = client.get('/menu')
    assert res.status_code == status.HTTP_200_OK

def test_place_order():
    client = fff.test_client()
    res = client.post('/orders', json={
        'username': 'sekayasin',
        'dish_name': 'Rolex',
        'order_quantity': 2,
        'total_order_cost': 60,
    })
    assert res.status_code == status.HTTP_201_CREATED

def test_get_orders():
    client = fff.test_client()
    res = client.get('/orders')
    assert res.status_code == status.HTTP_200_OK

# def test_menu_available():
#     ''' 
#     This tests whether the 3Fs Menu collection is not empty
#     '''
#     menu = models.Menu()
#     menu.add_menu('pilawo', '30K UGX')
#     assert len(menu.get_available_menu()) == 1


# def test_orders_available():
#     ''' 
#     This tests whether the 3Fs Menu collection is not empty
#     '''
#     orders = models.Orders()
#     orders.add_order('pilawo', 3, '90K UGX', 'sekayasin', '12A Kevina Rd')
#     assert len(orders.get_orders()) == 1

    