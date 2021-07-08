from flask import Flask
import random
app = Flask(__name__)

############################
@app.route('/')
def prizes():
    prizes = dict() 
    prizes = {1:5000, 2:1, 3:25000, 4:34, 5:500, 6:780, 7:300000, 8:43000, 9:3, 10: 0.4}
    number = random.randint (1, len(prizes.keys()))
    return str(prizes[number])


