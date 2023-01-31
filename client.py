import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = ('localhost', 3000)

client_socket.connect(host_port)
client_socket.sendall(bytes("Hello world from client side".encode('UTF-8')))
client_socket.close()
