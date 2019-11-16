from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route('/')
def hello():
    return "Raspberry pi List of working ips"


@app.route('/index')
def index():
    raspberries = mongo.db['rasps'].find()
    return render_template('index.html', title='Home', raspberries=raspberries)


@app.route('/saveip')
def saveip():
    name = request.args.get('name')
    ip = request.args.get('ip')
    mydict = {'name': name, 'ip': ip}
    mongo.db['rasps'].insert_one(mydict)
    return "ok"

@app.route('/clearlist')
def clear_all_rasp():
    mongo.db['rasps'].delete_many({})
    return "The list is cleared"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
