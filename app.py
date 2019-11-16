from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
# ips = {'raspberry1501':'10.0.0.7', 'raspberry1502':'10.0.0.3' }   # 'name':'ip'
ips = {}


@app.route('/')
def hello():
    return "Raspberry pi List of working ips"

@app.route('/index')
def index():
    raspberries = [{'name':name, 'ip': ips[name]} for name in ips ]

    return render_template('index.html', title='Home', raspberries=raspberries)


@app.route('/saveip')
def saveip():
    name = request.args.get('name')
    ip = request.args.get('ip')
    try:
        ips[name] = ip
    except Exception as e:
        print(e)

    return "ok"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)