import socket
import time

IP_ADDR = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP_ADDR, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('client address:', addr)
    data = conn.recv(BUFFER_SIZE)
    currentTime = " " + " updated !!! " + time.ctime(time.time()) + "\r\n"
    print(data.decode('utf-8'))
    data = data + currentTime.encode('ascii')
    coon.send(data) # echo
    conn.close()
