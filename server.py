
from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(.*[0-9].*[A-Z].*)|(.*[A-Z].*[0-9].*)$')
DOB_REGEX = re.compile(r'^((?:0[1-9])|(?:1[0-2]))\/((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/(\d{4})')
app = Flask(__name__)
app.secret_key = "whatever"
@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank.")
    elif not EMAIL_REGEX.match(request.form['email']):
 		flash("Invalid Email Address!")
    if len(request.form['fname']) < 1:
    	flash("First name cannot be blank.")
    elif not NAME_REGEX.match(request.form['fname']):
    	flash("Invalid first name")
    if len(request.form['lname']) < 1:
        flash("Last name cannot be blank.")
    elif not NAME_REGEX.match(request.form['lname']):
        flash("Invalid last name")
    if len(request.form['password']) < 9:
    	flash('Password must be 8 or more characters.')
    elif not PASSWORD_REGEX.match(request.form['password']):
    	flash('Password is invalid')
    if request.form['password'] != request.form['confpassword']:
        flash('Passwords must match')
    elif not DOB_REGEX.match(request.form['dob']):
        flash('Must enter dd/mm/yyyy')
    else:
    	flash("Success!")
    return redirect('/')
app.run(debug=True)