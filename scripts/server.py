import socket
from sys import exec_prefix
import time

HOST = '127.0.0.1'
PORT = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[Socket] Socket was created successfully')
except:
    print('[Socket] Socket faild to be creted')

try:
    s.bind((HOST, PORT))
    print(f'[Socket] Socket was binded successfully ({HOST}:{PORT})')
except:
    print('[Socket] Socket could not be binded')

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'[Connection] Connection made {address}')

    msg = 'Welcome to the server!!'

    clientsocket.send(bytes(msg, 'utf-8'))

    while True:
        msg = '[Status] OK'
        try:
            clientsocket.send(bytes(msg, 'utf-8'))
            time.sleep(1)
        except:
            print(f'[Connection] Client {address} has disconnected')
            break
