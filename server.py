from flask import Flask, render_template, request, jsonify
from random import randint
import os
import socket
import time
import multiprocessing

import tcpServer

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_init1')
def initial_game1():

    clientsocket = socket.socket()
    clientsocket.connect((host, 10000))

    msg = clientsocket.recv(1024)
    value = int(msg.decode('ascii'))
    clientsocket.close
    return jsonify(result = value)

@app.route('/_init2')
def initial_game2():

    clientsocket = socket.socket()
    clientsocket.connect((host, 20000))

    msg = clientsocket.recv(1024)
    value = int(msg.decode('ascii'))
    clientsocket.close
    return jsonify(result = value)

@app.route('/_init3')
def initial_game3():

    clientsocket = socket.socket()
    clientsocket.connect((host, 30000))

    msg = clientsocket.recv(1024)
    value = int(msg.decode('ascii'))
    clientsocket.close
    return jsonify(result = value)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/_random_numbers')
def random_numbers():
    return jsonify(result=randint(1, 5)) # 1 - 5


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

    host = socket.gethostname()

    p = multiprocessing.Process(target=tcpServer.start_tcpServer)
    p.start()
    
    print("Start Server...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, use_reloader=False)

