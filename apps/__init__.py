"""
Initialize Flask app

"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#this make query, way to give and receive 
#data between server and database, available in flask
#instead of using query, data can be CRUD in python /
#code. 
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager


app = Flask('apps')
#'Flask' module is installed in apps folder
# Flask
app.config.from_object('apps.settings.Production')

db = SQLAlchemy(app)
# apps folder having installation of Flask module
#make data be Created,... in python code 
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

import views, models
#guess: Export variable to views.py and models.py 
#usually class, function only can be imported. however, with 'import(last line)' 
#can import var
