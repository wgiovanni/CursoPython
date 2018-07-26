# -*- coding: utf-8 -*-
from wtforms import Form, StringField, validators

class ContactForm(Form):                      
	name=StringField("Nombre:",[validators.DataRequired(), validators.Length(min=4, max=25, message="Más de 25 caracteres")])
	phone=StringField("Telefono:",[validators.Length(min=1, max=20,message='Más de 20 carácteres')])
	email=StringField("Email:",[validators.Email(), validators.Length(min=-1, max=200, message='Más de 200 carácteres')])