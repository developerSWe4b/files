import socket

# Configuration
SERVER_IP = 'rngnx-110-226-183-27.a.free.pinggy.link'  # Replace with the IP address of your PC
PORT = 35723                # Port used by the server
FILE_PATH = 'screenshot.png'

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

print(f"Connected to server {SERVER_IP}:{PORT}")

# Open the file and send its contents
with open(FILE_PATH, 'rb') as f:
    while (chunk := f.read(4096)):  # Read in 4096-byte chunks
        client_socket.sendall(chunk)

print(f"File '{FILE_PATH}' sent successfully!")
client_socket.close()
