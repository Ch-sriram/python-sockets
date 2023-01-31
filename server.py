import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = ('localhost', 3000)

server_socket.bind(host_port)

server_socket.listen()

conn_obj, addr = server_socket.accept()

data = conn_obj.recv(1024)

print(str(data))

server_socket.close()
