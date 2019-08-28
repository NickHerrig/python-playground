import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    my_message = input('What message would you like to send?')
    s.sendall(my_message.encode())
    data = s.recv(1024)

print('Received', repr(data.decode()))
