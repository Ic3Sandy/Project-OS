import socket
import _thread
from random import randint
import os

host = socket.gethostname()
print("[Get hostname]: %s" % (host))

serversocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("[Create socket]: %s" % (serversocket1))

serversocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("[Create socket]: %s" % (serversocket2))

serversocket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("[Create socket]: %s" % (serversocket3))

port1 = int(os.environ.get('PORT', 10000))
serversocket1.bind((host, port1))

port2 = int(os.environ.get('PORT', 20000))
serversocket2.bind((host, port2))

port3 = int(os.environ.get('PORT', 30000))
serversocket3.bind((host, port3))


def thread(serversocket, number):

    print("[Start Thread]: ", number)
    while True:

        serversocket.listen(5)
        clientsocket, addr = serversocket.accept()
        # print("[Got connection]: ", addr)

        if(number == 1):
            random_num = randint(100, 110)

        elif(number == 2):
            random_num = randint(120, 130)

        else:
            random_num = randint(140, 150)

        print("[Thread]: %d Random Number: %d" % (number, random_num))

        msg = '%d' % random_num
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()


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

        _thread.start_new_thread(thread, (serversocket1, 1))
        _thread.start_new_thread(thread, (serversocket2, 2))
        _thread.start_new_thread(thread, (serversocket3, 3))

    except:

        print ("Error: unable to start thread")

    while True:
        pass