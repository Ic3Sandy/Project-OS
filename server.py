from flask import Flask, render_template, request, jsonify
from random import randint
import os

from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_random_numbers')
def random_numbers():
    return jsonify(result=randint(0, 20)) # 0 - 100

@app.route('/home')
def homepage():
    users = [
        {
            'name' : 'ice',
        },
        {
            'name' : 'ic3'
        },
        {
            'name' : 'Ic3Sandy'
        }
    ]
    return render_template('home.html', title='Home', users=users)
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, use_reloader=True)

