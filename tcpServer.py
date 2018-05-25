import socket
import _thread
from random import randint
import os

# Get hostname of pc
host = socket.gethostname()
print("[Get hostname]: %s" % (host))

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

list_port = [10000, 20000, 30000]

# Set port and bind the socket to address
serversocket1.bind((host, list_port[0]))

serversocket2.bind((host, list_port[1]))

serversocket3.bind((host, list_port[2]))

# Create function to return list of port
def def_port():
    return list_port

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