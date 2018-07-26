# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/wilke/prueba.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'dialect+driver://postgres:123456@localhost:5432/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contact(db.Model):

	__tablename__ = 'contact'

	id = db.Column('id', db.Integer, primary_key = True, nullable = False, autoincrement=True)
	name = db.Column('name', db.String(20), nullable = False)
	email = db.Column('email', db.String(20), nullable = False)
	phone = db.Column('phone', db.String(15), nullable = False)

def __repr__(self):
        return '<Contacts %r>' % self.name

def __init__(self, id, name, phone, email):
	self.id = id
	self.name = name
	self.phone = phone
	self.email = email

