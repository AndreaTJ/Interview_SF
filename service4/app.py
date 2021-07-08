from flask import Flask, render_template, jsonify
app = Flask(__name__)

import requests
api = 'http://service2:5003'
api2 = 'http://service3:5002'

###########################

@app.route('/')
def hello_internet():
    
    response = requests.get(api)
    country = response.text 


    response = requests.get(api2)
    money = response.text 

    money2 = 0 
    if len(country) in range (0,7):
        money2 = float(money)/25 +1
        money2 = str(round(money2,2))
    else: 
        money2 = float(money)*5
        money2 = str(round(money2,2))



    result_generated = dict() 
    result_generated = { country: money2}
    result_generated = jsonify ( result_generated)
    result_2 = jsonify (country, money2)
    return  result_2
