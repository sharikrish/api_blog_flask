from os import environ

class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')
    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql://scireptor@localhost/test_data_mouse_B6'
    SQLALCHEMY_TRACK_MODIFICATIONS = True