import os

from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://heroku_4ctp328z:DiscWorld12@ds041228.mlab.com:41228/heroku_4ctp328z"
mongo = PyMongo(app)
db = mongo.get_default_database()
my_rasps = db['rasps']

@app.route('/')
def hello():
    return "Raspberry pi List of working ips"


@app.route('/index')
def index():
    raspberries = my_rasps.find()
    return render_template('index.html', title='Home', raspberries=raspberries)


@app.route('/saveip')
def saveip():
    name = request.args.get('name')
    ip = request.args.get('ip')
    mydict = {'name': name, 'ip': ip}
    my_rasps.insert_one(mydict)
    return "ok"

@app.route('/clearlist')
def clear_all_rasp():
    my_rasps.delete_many({})
    return "The list is cleared"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
