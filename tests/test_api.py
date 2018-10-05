import pytest
from datetime import datetime
from flask import Response, json
from api import fff, routes, status


def test_index():
    client = fff.test_client()
    res = client.get('/')
    assert res.status_code == status.HTTP_302_FOUND

    