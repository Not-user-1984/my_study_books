
import socket

# Constants
SERVER_PORT = 12000
BUFFER_SIZE = 2048

# Create a UDP socket and bind it to the server port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', SERVER_PORT))

# Print a message to indicate that the server is ready to receive messages
print("The server is ready to receive messages")

# Receive and process incoming messages
while True:
    message, client_address = server_socket.recvfrom(BUFFER_SIZE)

    # Decode the received message from bytes to string
    message = message.decode('utf-8')

    # Print the received message and the client's address to the console
    print(f"Message received from {client_address}: {message}")

    # Send a response back to the client
    response = f"Server received your message: {message}"
    server_socket.sendto(response.encode('utf-8'), client_address)
