import asyncio
from socket import *

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """
    Обрабатывает соединение с клиентом.

    :param reader: объект асинхронного потока чтения.
    :type reader: asyncio.StreamReader

    :param writer: объект асинхронного потока записи.
    :type writer: asyncio.StreamWriter
    """
    data = await reader.read(1024)
    massage = data.decode()

    modified_massage = massage.upper().encode()
    writer.write(modified_massage)
    writer.close()
    await writer.wait_closed()
async def main():
    """
    Создает TCP сокет, биндит его на 12000 порт и обрабатывает входящие соединения асинхронно.
    """

    # Создаем TCP сокет
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Биндим сокет на 12000 порт
    server_socket.bind(('localhost', 12000))

    # Слушаем входящие соединения
    server_socket.listen()

    # Обрабатываем входящие соединения асинхронно
    while True:
        client_socket, addr = await loop.sock_accept(server_socket)
        print(f"Подключение с адресом {addr} установлено")

        # Создаем асинхронные потоки чтения и записи для клиентского сокета
        reader, writer = await asyncio.open_connection(sock=client_socket)

        # Обрабатываем соединение с клиентом в отдельном асинхронном потоке
        asyncio.create_task(handle_client(reader, writer))

if __name__ == '__main__':
    # Создаем цикл событий и запускаем сервер
    asyncio.run(main())