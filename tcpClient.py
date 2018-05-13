import socket
import time

# s1 = socket.socket()
# print("[Create socket]: %s" % s1)
# s2 = socket.socket()
# print("[Create socket]: %s" % s2)

host = socket.gethostname()
print("[Hostname]: %s" % host)

port1 = 5000
# s1.connect((host, port1))
port2 = 6000
# s2.connect((host, port2))

def client(s):
    print("[Connection]: %s" % s)
    msg = s.recv(1024)
    print("Data receives: %s" % msg.decode('ascii'))
    s.close

if __name__ == '__main__':
    while True:
        s1 = socket.socket()
        s2 = socket.socket()
        s1.connect((host, port1))
        s2.connect((host, port2))
        client(s1)
        client(s2)
        time.sleep(1)