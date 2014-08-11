"""
settings.py

Configuration for Flask app

"""


class Config(object):
    # Set secret key to use session
    # setting
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False
    #


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "helloavakoo@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=helloavakoo:helloavakoo-instance'
    # database access address connecting between actual database and Flask
    # database=flask(server) help flask to find database
    migration_directory = 'migrations'
