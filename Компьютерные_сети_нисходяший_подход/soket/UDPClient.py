
import socket

# Constants
SERVER_ADDRESS = "localhost"
SERVER_PORT = 12000

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get user input for the message to send
message = 'привет'

# Send the message to the server
client_socket.sendto(message.encode('utf-8'), (SERVER_ADDRESS, SERVER_PORT))

# Receive the modified message from the server and print it
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode('utf-8'))

# Close the socket
client_socket.close()