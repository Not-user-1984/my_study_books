import os
import threading

print(f"Исполнятся Python-процесс и идентифиикатором : {os.getgid()}")

total_threading = threading.active_count()

threading_name = threading.current_thread().name

print(f'В данный момент Python исполняет {total_threading} поток(ов)')
print(f'Имя текушего потока {threading_name}')
