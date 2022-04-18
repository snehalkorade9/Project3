"""This test the homepage"""
import os

import logdir as logdir


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200

def test_log_creation():
    """check if info.log is created"""
    root = os.path.dirname(os.path.abspath(__file__))
    print (os.path.join(root, "/flask_auth_logging/app/logs"))
    assert os.path.exists(os.path.join(root, "/flask_auth_logging/app/logs")) == True

def test_log_creation():
    """check if info.log is created"""
    root = os.path.dirname(os.path.abspath(__file__))
    log1 = os.path.join(root, "/flask_auth_logging/app/logs", "info.log")
    assert os.path.exists(log1) == True