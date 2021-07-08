from flask import Flask
import random
app = Flask(__name__)

##############################################

@app.route('/')
def hello_internet():
    country = dict() 
    country= {1:"Brazil", 2:"Mexico", 3:"Bahamas", 4: "San Francisco", 5: "Miami", 6: "Madrid", 7:"Pekin", 8: "Dubai", 9: "Paris", 10: "Rome"}

    number = random.randint (1, len(country.keys()))

    return country[number]

