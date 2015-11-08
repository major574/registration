
from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
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
    else:
        flash("Success!")
    return redirect('/')

    # if len(request.form['urname']) < 1:
    # 	flash("Name cannot be blank.")
    # elif not NAME_REGEX.match(request.form['urname']):
    # 	flash("Invalid Name")
    # else:
    # 	flash("Succes!")
    # return redirect('/')
app.run(debug=True)