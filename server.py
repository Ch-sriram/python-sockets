import socket

# Create a socket at the server side
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server's IP and PORT
host_port = ('localhost', 3000)

# This time (unlike client side code, where it's trying to connect to `localhost:3000`), 
# we're going to bind this `host_port` to the created `server_socket` defined above. 
# The reason why we bind is because, this server's socket address is the combination of the 
# host and port defined above, to which the client is trying to connect to.
server_socket.bind(host_port)

# The server has to listen to any incoming request(s), and as soon as a request has reached this
# `server_socket` -- the server will accept the request. Also, the listen() call is like an infinite
# while loop -- it keeps on listening until there's a request it found from any client.
server_socket.listen()

# Accept will return a tuple (connection_object, address). 
# Print the contents of each to see what's there inside each object.
conn_obj, addr = server_socket.accept()

# Set a max limit to the data we can receive per chunk: for this case, it's 1024B (or 1KB).
data = conn_obj.recv(1024)

print(str(data))

# Close the server side socket resource.
server_socket.close()
