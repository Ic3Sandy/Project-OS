import socket
import time

host = socket.gethostname()
print("[Hostname]: %s" % host)

port1 = 10000
port2 = 20000
port3 = 30000


def client(clientsocket, numder):

    # print("[Connection]: %s" % clientsocket)
    msg = clientsocket.recv(1024)
    print("Thread %d Random number: %s" % (numder, msg.decode('ascii')))
    clientsocket.close


if __name__ == '__main__':

    while True:

        clientsocket1 = socket.socket()
        clientsocket2 = socket.socket()
        clientsocket3 = socket.socket()

        clientsocket1.connect((host, port1))
        clientsocket2.connect((host, port2))
        clientsocket3.connect((host, port3))

        client(clientsocket1, 1)
        client(clientsocket2, 2)
        client(clientsocket3, 3)

        time.sleep(1)
