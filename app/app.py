# flask_web/app.py
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/one', defaults={'path': ''})
@app.route('/one/', defaults={'path': ''})
@app.route('/one/<path:path>')
def index1(path):
    return "Hello, World! one! path: %s" % path

@app.route('/two', defaults={'path': ''})
@app.route('/two/', defaults={'path': ''})
@app.route('/two/<path:path>')
def index2(path):
    return "Hello, World! two! path: %s" % path

@app.route('/admin', defaults={'path': ''})
@app.route('/admin/', defaults={'path': ''})
@app.route('/admin/<path:path>')
def index3(path):
    return "Hello, World! admin! path: %s" % path





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

