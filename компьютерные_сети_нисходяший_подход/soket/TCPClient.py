import asyncio
import socket

# Constants
SERVER_ADDRESS = "localhost"
SERVER_PORT = 12000
BUFFER_SIZE = 1024


async def handle_message(client_socket):
    """
    Отправляет сообщение на сервер и получает ответное сообщение.

    :param client_socket: Сокет клиента.
    :type client_socket: socket.socket
    """

    # Get user input for the message to send
    message = input("Введите строку в нижнем регистре: ")

    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

    # Receive the modified message from the server and print it
    modified_message = await loop.sock_recv(client_socket, BUFFER_SIZE)
    print(f"От сервера: {modified_message.decode('utf-8')}")


async def main():
    """
    Создает TCP сокет, подключается к серверу и обрабатывает входящие сообщения.
    """

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

    # Call the handle_message function asynchronously
    await handle_message(client_socket)

    # Close the socket
    client_socket.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())