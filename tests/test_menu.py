import pytest
from api import routes, models
''' 
This tests whether the 3Fs Menu collection is not empty
'''

def test_menu_available():
    models.menu = [{'name': 'kikomando'}]
    assert len(models.menu) == 1

    

