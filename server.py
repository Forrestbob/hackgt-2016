from flask import Flask, render_template, url_for, request, redirect, session, flash, g, json
from functools import wraps
import sqlite3
app = Flask(__name__)
#app.database = "sample.db"
#app.secret_key = "oh baby"
import requests 
from flask_bcrypt import Bcrypt  
bcrypt = Bcrypt(app)
                         
@app.route('/')           
def welcome():
  return render_template('login.html')

@app.route('/login', methods=['POST'])                      
def login():
  username = request.form['username']
  password = request.form['password']
  user_query = "SELECT * FROM flyers WHERE username = :username LIMIT 1"
  query_data = { 'username': username }
  user = mysql.query_db(user_query, query_data) # user will be returned in a list
  if bcrypt.check_password_hash(user[0]['password'], password):
  	session['uuid']=user['uuid']
  else:
  	flash('incorrect log in')
  params = {'apikey':'27AicFy3VpXxTKAln2LRuCvZesfAebtZ' }
  results = requests.get('https://demo30-test.apigee.net/v1/hack/corporate/passengers', params=params)
  results = results.json()
  results = results['entities']
  user = {}
  for each in results:
    if each['uuid']=='fc163a5a-7f82-11e6-bb9a-cdff87b7f965':
      user['flight_number'] = each['freqFlierNumber']
      print user['flight_number']
  return user['flight_number']
  
  # set flash error message and redirect to login page

@app.route('/logout', methods=['GET'])
def logout():
  session.pop('uuid')
  return redirect('/')



  
app.run(debug=True)      