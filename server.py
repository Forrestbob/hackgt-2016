from flask import Flask, render_template, url_for, request, redirect, session, flash, g, json, jsonify
from functools import wraps
import sqlite3
app = Flask(__name__)
app.database = "DeltaDB1.db"
app.secret_key = "oh baby"
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
  g.db = connect_db()
  user1 = g.db.execute("SELECT * FROM Flyers WHERE username=?", (username,))
  print user1
  user = [dict(
    first_name= row[1],
    last_name= row[2],
    username= row[5],
    password= row[4],
    uuid= row[0],
    points= row[3]

    ) for row in user1.fetchall()]
  print user
  print user[0]
  if bcrypt.check_password_hash(user[0]['password'], password) == False:
    flash('incorrect log in')
    return redirect('/')
  params = {'apikey':'27AicFy3VpXxTKAln2LRuCvZesfAebtZ' }
  results = requests.get('https://demo30-test.apigee.net/v1/hack/corporate/passengers', params=params)
  results = results.json()
  results = results['entities']
  for each in results:
    if each['uuid']=='fc163a5a-7f82-11e6-bb9a-cdff87b7f965':
      user[0]['flight_number'] = each['freqFlierNumber']
      flight = dict(
        ticket_number= each['ticketNumber'],
        departure= "Hartsfield-Jackson Atlanta International Airport",
        departure_time= "Friday August 9, 9:00pm EST",
        destination= "Los Angeles International Airport",
        arrival_time= "Saturday August 10, 12:00am EST"
      )
      if hasattr(user[0], 'flights'):
        user[0]['flights'].append(flight)
      else:
        user[0]['flights']= [flight]
  session['current_user'] = user
  return jsonify(session['current_user'])
  
  # set flash error message and redirect to login page

@app.route('/logout', methods=['GET'])
def logout():
  session.pop('current_user')
  return redirect('/')



  
def connect_db():
        return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True) 
