import socket

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and Port of the Server
host_port = ('localhost', 3000)

# NOTE: The socket for the client will be created with a port that's assigned by the OS
#       There's no need to assign a port by the user.
# Connect to the server using `host_port`
client_socket.connect(host_port)

# Send the required data to the Server
client_socket.sendall(bytes("Hello world from client side".encode('UTF-8')))

# Close the client's socket resource
client_socket.close()
