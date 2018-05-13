import socket
import _thread

serversocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[Create socket]: %s" % (serversocket1))

serversocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[Create socket]: %s" % (serversocket2))

host = socket.gethostname()
print("[Get hostname]: %s" % (host))

port1 = 5000
serversocket1.bind((host, port1))

port2 = 6000
serversocket2.bind((host, port2))


def thread(serversocket, number):
    while True:
        serversocket.listen(5)
        clientsocket, addr = serversocket.accept()
        print("[Thread]: ", number)
        print("[Connection]: %s, %s" % (clientsocket, addr))
        print("[Got connection]: ", addr)
        msg = 'Thank you for connection %d' % number
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()

if __name__  == '__main__':
    try: 
        _thread.start_new_thread(thread, (serversocket1, 1))
        _thread.start_new_thread(thread, (serversocket2, 2))
    except:
        print ("Error: unable to start thread")
    while True:
        pass