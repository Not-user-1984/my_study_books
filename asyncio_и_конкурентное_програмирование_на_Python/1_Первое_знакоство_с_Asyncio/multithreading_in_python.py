import threading


def hello_from_thread():
    print(f'Привет  из потока {threading.current_thread()}')


hello_threading = threading.Thread(
    target=hello_from_thread)

hello_threading.start()

total_threading = threading.active_count()

threading_name = threading.current_thread().name

print(f'В данный момент Python исполняет {total_threading} поток(ов)')
print(f'Имя текушего потока {threading_name}')

hello_threading.join()
