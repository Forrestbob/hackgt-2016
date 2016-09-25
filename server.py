from flask import Flask, render_template, url_for, request, redirect, session, flash, g, json, jsonify
from functools import wraps
from requests.auth import HTTPBasicAuth
import sqlite3
from rauth import OAuth2Service
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
        departure= "6000 N Terminal Pkwy, Atlanta, GA 30320",
        departure_time= "Friday August 9, 9:00pm EST",
        destination= "1 World Way, Los Angeles, CA 90045",
        arrival_time= "Saturday August 10, 12:00am EST",
        
      )
      if hasattr(user[0], 'flights'):
        user[0]['flights'].append(flight)
      else:
        user[0]['flights']= [flight]
  session['current_user'] = user
  return render_template('dashboard.html')
  
  # set flash error message and redirect to login page

@app.route('/logout', methods=['GET'])
def logout():
  session.pop('current_user')
  return redirect('/')

@app.route('/estimate/<int:index>')
def estimate(index):
  index = 0
  url='https://maps.googleapis.com/maps/api/geocode/json'
  params1={'sensor':'false','address': session['current_user'][0]['flights'][index]['destination']}
  results1 = requests.get(url, params=params1)
  destination = results1.json()['results'][0]['geometry']['location']
  session['dest_long_lat'] = {'long':destination['lng'], 'lat':destination['lat']}

  params2={'sensor':'false','address': session['current_user'][0]['flights'][index]['departure']}
  results2 = requests.get(url, params=params2)
  departure = results2.json()['results'][0]['geometry']['location']
  session['dept_long_lat'] = {'long':departure['lng'], 'lat':departure['lat']}
  session['hide_or_show'] = "hidden"
  return render_template('estimate.html', index=index)

@app.route('/search', methods=['POST'])
def search():
  url='https://maps.googleapis.com/maps/api/geocode/json'
  #textInput = request.form['pac-input']
  session['objective'] = request.form['destination']
  is_sensor= "false"
  payload = {'address': request.form['destination'], 'sensor': is_sensor }
  req = requests.get(url, params=payload)
  output = req.json()

  results_list = output['results']
  results_status = output['status']

  lat = results_list[0]['geometry']['location']['lat']
  lng = results_list[0]['geometry']['location']['lng']
  destination = {'lat':lat, 'lng':lng}
  origin = {'lat': session['dept_long_lat']['lat'], 'lng': session['dept_long_lat']['long']}
  url2= 'https://api.lyft.com/v1/eta'


  #return lat
  params1 = {'start_lat': session['dept_long_lat']['lat'], 'start_lng':session['dept_long_lat']['long'], 'end_lat': lat , 'end_lng': lng }
  params2 = {'lat': session['dept_long_lat']['lat'], 'lng':session['dept_long_lat']['long']}
  timing = requests.get('https://api.lyft.com/v1/eta', params=params2,headers={
        'Authorization': 'Bearer %s' % session['token']
    })
  timing = timing.json()
  pricing = requests.get('https://api.lyft.com/v1/cost', params=params1,  headers={
        'Authorization': 'Bearer %s' % session['token']
    })
  print pricing
  pricing = pricing.json()
  for each in pricing['cost_estimates']:
    if each['ride_type'] == 'lyft':
      pricing = int(each['estimated_cost_cents_max'])
  print timing
  for each in timing['eta_estimates']:
    if each['ride_type'] == 'lyft':
      timing = int(each['eta_seconds'])
 
  session['hide_or_show']='block'
  print pricing
  print timing
  return render_template("estimate.html", pricing=pricing, timing=timing, origin=origin, destination=destination)

@app.route('/lyft')
def step1():
  lyft_api = OAuth2Service(
     client_id='TgLMk7SiXddO',
     client_secret='SANDBOX-7_1kYCpmzzlHpTYv_z8E_PaXFFWeupgi',
     name='HACK GT 2016',
     authorize_url='https://api.lyft.com/oauth/authorize',
     access_token_url='https://api.lyft.com/oauth/token',
     base_url='https://api.lyft.com/v1/'
     )
  parameters = {
    'response_type': 'code',
    'redirect_uri':'https://1d96fd3c.ngrok.io/step2',
    'scope': 'rides.request profile rides.read public',
    'client_id':'TgLMk7SiXddO',
    'state':{}
    }
  login_url = lyft_api.get_authorize_url(**parameters)
  return render_template('estimate.html', login=login_url)


@app.route('/step2', methods=['GET'])
def step2():
  parameters = {
    'redirect_uri':'https://1d96fd3c.ngrok.io/step2',
    'code': request.args.get('code'),
    'grant_type': 'authorization_code'
    }
  response=requests.post(
    'https://api.lyft.com/oauth/token',
    auth=('TgLMk7SiXddO','SANDBOX-7_1kYCpmzzlHpTYv_z8E_PaXFFWeupgi'),
    data=parameters
    )
  print response.text
  access_token = response.json().get('access_token')
  session['token'] = access_token
  return access_token

@app.route('/create_ride', methods=['POST'])
def create_ride():
  price = request.form['price']
  destination = request.form['destination']
  origin = request.form['origin']
  print origin
  print destination
  lyft='lyft'

  params=dict( ride_type =lyft, origin=origin ,destination=destination)
 
  
  results = requests.post('https://api.lyft.com/v1/rides', params=params,headers={
        'Authorization': 'Bearer %s' % session['token']
    })



  result = results.json()
  print result
  g.db = connect_db()
  balance = g.db.execute("SELECT FlyerPoints - ? AS BALANCE FROM Flyers WHERE uuid=?", (price,session['current_user'][0]['uuid'],))
  balance = [dict(points= row[0]) for row in balance.fetchall()]
  print balance
  return render_template('confirmation.html', price=price, result=result, balance=balance)
  

  
def connect_db():
  return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True) 
