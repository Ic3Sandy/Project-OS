from flask import Flask, render_template, request, jsonify
from random import randint
import os
import socket
import multiprocessing
import signal
import sys

# Create Flask module and set static url path
app = Flask(__name__, static_url_path='/static')
PORT = int(os.environ.get('PORT', 5000))

# Create Process object with target start_tcpServer function
if PORT == 5000:
    import tcpServer
    p = multiprocessing.Process(target=tcpServer.start_tcpServer)

list_port = [10000, 20000, 30000]

# Connect URL to index function that render index.html page
@app.route('/', methods=['GET'])
def index():
    port = tcpServer.def_port()
    list_port[0] = port[0]
    list_port[1] = port[1]
    list_port[2] = port[2]
    return render_template('index.html')

# Connect URL to initial_game that create socket to connect tcpServer.py
# and return value that receive from host
@app.route('/_init', methods=['GET'])
def initial_game():

    # Get value from key name 'socket' in dictionary that collaborate with myscript.js
    socket_num = request.args.get('socket', 0, type=int)
    
    port = list_port[0]
    random_num = randint(100, 110)

    if(socket_num == 2):
        port = list_port[1]
        random_num = randint(120, 130)

    elif(socket_num == 3):
        port = list_port[2]
        random_num = randint(140, 150)

    if PORT != 5000:
        return jsonify(result = random_num)

    # Create socket and connect to host
    clientsocket = socket.socket()
    clientsocket.connect((host, port))

    # Read data from buffer and decode it
    msg = clientsocket.recv(1024)
    value = int(msg.decode('ascii'))

    # Close connection
    clientsocket.close

    # Return Response object that have result = value
    return jsonify(result = value)

# Connect URL to _random_number that return random number 1 to 5
@app.route('/_random_numbers', methods=['GET'])
def random_numbers():
    return jsonify(result=randint(1, 5)) # random 1 - 5

# Create signal_handler function that if connection is interrupt by user(use ctrl+C)
# it will terminate process and end 
def signal_handler(signal, frame):
        print('Process was kill!')
        print('Good Bye')
        p.terminate()
        sys.exit(0)


if __name__ == '__main__':    

    # Get hostname of PC
    host = socket.gethostname()

    # Start Process with target start_tcpServer function
    if PORT == 5000:
        p.start()

    # Set handler for signal that is interrupt from keyboard
    signal.signal(signal.SIGINT, signal_handler)

    print("Start Server...")

    # Run application
    app.run(host='0.0.0.0', port=PORT, use_reloader=False)
    
    

