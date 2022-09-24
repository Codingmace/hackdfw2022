import json
from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)

def writeHash():
	import hashlib
	f = open('people.csv')
	g = open('newPeople.csv', 'w')
	lines = f.readlines()
	for line in lines:
		split = line.split(',')
		person = split[0]
		myHash = hashlib.md5(bytes(person, 'utf-8')).hexdigest()
		g.write(line.strip() + ',' + myHash +"\n")
		g.flush()
		print(myHash)

@app.route('/')
def index():
	return json.dumps({'name': 'this'})

loginName = "Doctor A"
password = "mine"
@app.route("/login", methods = ['POST','GET'])
def login():
	if request.method == 'POST':
		loginName = request.form['username']
		password = request.form['password']
		return '''<form method = "post">
		<p>Enter Name:</p>
		<p><input type = "text" name = "username" /></p>
		<p>Enter Website:</p>
		<p><input type = "text" name = "password" /></p>
		<p><input type = "submit" value = "submit" /></p>
		</form>'''
	if request.method=='GET':
		return "Get is not valid"
	return "Something went wrong"

@app.route("/dashboard" , methods=['GET'])
def myDash():
	if loginName == "" or password == "":
		return redirect(url_for('login'))
	if 'Doctor' in loginName:
		f = open('peoples.csv')
		names = f.readline()
		DocIndex = -1
		splits = names.split(',')
		for i in range(0, len(splits)):
			if splits[i] == loginName:
				print('Found at index',i )
				DocIndex = i
		if DocIndex == -1:
			return "Doctor not Found"
		lines = f.readlines()
		toDo = []
		hashes = []
		for line in lines:
			cur = line.split(',')[DocIndex]
			if cur.lower() == "pending":
				toDo.append(line.split(',')[0])
				hashes.append(line.split(',')[-1])
				print("Check if in the drafts")
				print("Grab from other database if not found")
		return toDo

@app.route('verify', method=['GET'])
def verification():
	f = open('orders.csv', 'r')
	print('Get the most recent order')
	print("Then from that order and past order we determine if the number is off and was mistyped to have a faster response time to incorrect input")
app.run(debug=True)