# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, json, flash, redirect, url_for 
from contact_model import db, Contact
from forms import ContactForm


#Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/wilke/prueba.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route(r'/', methods=['GET'])
def contact_book():
	contacts = Contact.query.all()
	return render_template('contact_book.html', contacts = contacts)

@app.route(r'/add', methods=['GET','POST'])
def add_contact():
	form = ContactForm(request.form)
	if request.method == 'POST' and form.validate():
		#myContact = Contact(name=request.form.get('name'),
		#	phone=request.form.get('phone'),
		#	email=request.form.get('email'))
		myContact = Contact()
		form.populate_obj(myContact)
		db.session.add(myContact)
		try:
			db.session.commit()
			flash('Contacto creado satisfactoriamente', 'success')
			return redirect(url_for('contact_book'))
		except:
			db.session.rollback()
			flash('Error al generar contacto', 'danger')		

	return render_template('add_contact.html')


@app.route(r'/edit/<uid>', methods = ['GET', 'POST'])
def edit_contact(uid):
	contact = Contact.query.get(uid)
	form = ContactForm(request.form)
	if request.method == 'POST' and form.validate():
		myContact = Contact()
		form.populate_obj(myContact)
		contact.name = myContact.name
		contact.phone = myContact.phone
		contact.email = myContact.email
		try:
			db.session.add(contact)
			db.session.commit()
			flash('Contacto actualizado satisfactoriamente', 'success')
			#return redirect(url_for('contact_book'))
		except:
			db.session.rollback()
			flash('Error al generar contacto', 'danger')

	return render_template('edit_contact.html', contact = contact)


@app.route(r'/contacts/<uid>', methods = ['GET'])
def detail_contact(uid):
	contact = Contact.query.get(uid)
	return render_template('contact.html', contact = contact)


@app.route(r'/delete/<id>', methods = ['POST'])
def delete_contact(id):
	try:
		myContact = Contact.query.get(id)
		print(myContact.id)
		db.session.delete(myContact)
		db.session.commit()
		flash('Delete successfully.', 'danger')
	except:
		db.session.rollback()
		flash('Error delete  contact.', 'danger')

	return redirect(url_for('contact_book'))

	

if __name__ == '__main__':
	app.run()