# Process state:
# new -> ready -> running -> (terminated or waiting -> running)

# create sub process
# sub process need time to create and during this time, the main process continues
import os
import time
from multiprocessing import Process
def one():
    print(f"One process id:{os.getpid()}, parent process id{os.getppid()}:")

def two():
    print(f"Two process id:{os.getpid()}, parent process id{os.getppid()}:")

if __name__ == '__main__':
    print(f"main process: {os.getpid()}")

    p1 = Process(target=one)
    p2 = Process(target=two)
    p1.start()
    print(p1.is_alive()) # check whether a process is alive or not
    p1.join()
    p2.start()
    p2.join()

    print(p1.is_alive())

# processes does not share resources or independent (unlike thread, process is processed on each core)
l1 = []
def fun1():
    for i in range(3):
        l1.append(i)
        time.sleep(1)
    print(f"fun1: {l1}\n", end="")

def fun2():
    for i in range(3):
        l1.append(i)
        time.sleep(1)
    print(f"fun2: {l1}\n", end="")

if __name__ == '__main__':
    p1 = Process(target=fun1)
    p2 = Process(target=fun2)
    p1.start()
    p2.start()