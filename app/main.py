"""
Simple Http server
"""

import socket
import os

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

#create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    #wait for client connections
    client_connection, address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
        filename = '/index.html'
    
    try:
    
        # Get the content of htdocs/index.html
        fin = open('../htdocs'+filename)
        content = fin.read()
        fin.close()

        # Send HTTP response 
        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        
    client_connection.sendall(response.encode())
    client_connection.close()

# close the socket
server_socket.close()


