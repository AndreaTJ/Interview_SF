from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv 
app = Flask(__name__)

api = 'http://service4:5001'


###############


app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:root@34.68.21.59/flaskdb"

db = SQLAlchemy(app)

class Duo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country= db.Column(db.String(30), nullable=False)
    money = db.Column(db.String(30), nullable=False)

db.drop_all
db.create_all() 



@app.route('/')
def hello_internet():
    
    response = requests.get(api)
    generated = response.json() 

    country, money = generated
    db.session.add(Duo( country= country, money=money))
    db.session.commit()

    query = db.session.query(Duo).order_by(Duo.id.desc()).all()
    
    return render_template ( "base.html" , result=query, country=country, money=money)

    
