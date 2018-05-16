from flask import Flask, render_template, request, jsonify
from random import randint
import os
import socket
import multiprocessing
import signal
import sys
import tcpServer

app = Flask(__name__, static_url_path='/static')

p = multiprocessing.Process(target=tcpServer.start_tcpServer)

list_port = [10000, 20000, 30000]


@app.route('/', methods=['GET'])
def index():
    port = tcpServer.def_port()
    list_port[0] = port[0]
    list_port[1] = port[1]
    list_port[2] = port[2]
    return render_template('index.html')


@app.route('/_init', methods=['GET'])
def initial_game():

    socket_num = request.args.get('socket', 0, type=int)
    
    port = list_port[0]

    if(socket_num == 2):
        port = list_port[1]

    elif(socket_num == 3):
        port = list_port[2]

    clientsocket = socket.socket()
    clientsocket.connect((host, port))

    msg = clientsocket.recv(1024)
    value = int(msg.decode('ascii'))
    clientsocket.close

    return jsonify(result = value)


@app.route('/_random_numbers', methods=['GET'])
def random_numbers():
    return jsonify(result=randint(1, 5)) # random 1 - 5


def signal_handler(signal, frame):
        print('Process was kill!')
        print('Good Bye')
        p.terminate()
        sys.exit(0)


if __name__ == '__main__':    

    host = socket.gethostname()

    p.start()

    signal.signal(signal.SIGINT, signal_handler)

    print("Start Server...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, use_reloader=False)
    
    

