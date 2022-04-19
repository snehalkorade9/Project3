import os

import sys
from click.testing import CliRunner

from app import create_log_folder, create_database

runner = CliRunner()


def test_create_log_folder():
    response = runner.invoke(create_log_folder, [])
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(root)
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, './/app/logs')
    print(logdir)
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True

def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True

def test_create_log_flask():
    # set the name of the apps log folder to logs
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, './/app/logs', 'flask.log')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True

def test_create_log_errors():
    # set the name of the apps log folder to logs
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, './/app/logs', 'errors.log')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True

def test_create_log_myapp():
    # set the name of the apps log folder to logs
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, './/app/logs', 'myapp.log')
    print(logdir)
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True

def test_create_log_sqlalchemy():
    # set the name of the apps log folder to logs
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, './/app/logs', 'sqlalchemy.log')
    print(logdir)
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True


#Test werkzeug file creation
def test_create_log_werkzeug():
    # set the name of the apps log folder to logs
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, './/app/logs', 'sqlalchemy.log')
    print(logdir)
    # make a directory if it doesn't exist testpush
    assert os.path.exists(logdir) == True