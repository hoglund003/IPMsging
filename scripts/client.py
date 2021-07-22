import socket

s = socket.socket()

ip = '127.0.0.1'
port = 12345

try:
    s.connect((ip, port))
    print(f'Connected')
except:
    print('Could not connect')

while True:
    msg = s.recv(1024).decode('utf-8')
    print(msg)
