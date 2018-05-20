import socket
import _thread
from random import randint
import os
# Get hostname of pc
host = socket.gethostname()
print("[Get hostname]: %s" % (host))
ports =[10000, 20000, 30000]

# def get_open_port():
#         import socket
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind(("",0))
#         s.listen(1)
#         port = s.getsockname()[1]
#         s.close()
#         return port

# ports =[get_open_port(), get_open_port(), get_open_port()]

# Create socket with address family AF_INET and sock type SOCK_STREAM
# and set socket option
serversocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("[Create socket]: %s" % (serversocket1))

serversocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("[Create socket]: %s" % (serversocket2))

serversocket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("[Create socket]: %s" % (serversocket3))

# Set port and bind the socket to address
port1 = int(os.environ.get('PORT', ports[0]))
serversocket1.bind((host, port1))
# ports[0] = serversocket1.getsockname()[1]

port2 = int(os.environ.get('PORT', ports[1]))
serversocket2.bind((host, port2))
# ports[1] = serversocket2.getsockname()[1]

port3 = int(os.environ.get('PORT', ports[2]))
serversocket3.bind((host, port3))
# ports[2] = serversocket3.getsockname()[1]

# Create function to return list of port
def def_port():
    return ports

# Create thread function
def thread(serversocket, number):

    print("[Start Thread]: ", number)
    while True:
        # Enable server to accept connections and assign queue with 5
        serversocket.listen(5)

        # Socket be bound to an address and listening for connections
        clientsocket, addr = serversocket.accept()
        print("[Got connection]: ", addr)

        if(number == 1):
            random_num = randint(100, 110)

        elif(number == 2):
            random_num = randint(120, 130)

        else:
            random_num = randint(140, 150)

        print("[Thread]: %d Random Number: %d" % (number, random_num))

        msg = '%d' % random_num
        # Encode massage to assci code
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()

# Create start_tcpServer that use by server.py to start a thread
def start_tcpServer():

    try: 

        _thread.start_new_thread(thread, (serversocket1, 1))
        _thread.start_new_thread(thread, (serversocket2, 2))
        _thread.start_new_thread(thread, (serversocket3, 3))

    except:

        print ("Error: unable to start thread")

    while True:
        pass


if __name__  == '__main__':

    try: 

        #Start a thread that execute thread function
        _thread.start_new_thread(thread, (serversocket1, 1))
        _thread.start_new_thread(thread, (serversocket2, 2))
        _thread.start_new_thread(thread, (serversocket3, 3))

    except:

        print ("Error: unable to start thread")

    while True:
        pass