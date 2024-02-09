import multiprocessing
import os


def hello_from_multiprocessin():
    print(f'Привет  из дочернего процесса  {os.getpid()}')


if __name__ == '__main__':
    hello_multiprocessin = multiprocessing.Process(
        target=hello_from_multiprocessin)
    hello_multiprocessin.start()
    print(f'Привет  из родительского процесса  {os.getpid()}')
    hello_multiprocessin.join()
