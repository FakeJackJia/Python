import threading
import time
from threading import Thread

# Define our thread
class OurThread(Thread):
    def run(self): # will be called automatically when this sub thread is processed
        print(f"Current thread: {threading.current_thread().name}")

t1 = OurThread()
t2 = OurThread()
t1.start() # start() indicates this function in this sub thread is ready for CPU to process
t2.start()

# Note: the process of threads is unordered, it is decided by the cpu
def task():
    time.sleep(1)
    print(f"thread: {threading.current_thread().name}\n", end="")

for i in range(5):
    t = Thread(target=task)
    t.start()

# resource can be shared among threads
l1 = []

def write():
    for j in range(5):
        l1.append(j)
        time.sleep(0.2)
    print("Write", l1)

def read():
    print("Read", l1)

t1 = Thread(target=write)
t2 = Thread(target=read)
t1.start()
#t1.join() by using this, it will until this thread finished, hence, t2 will read whole list this time
t2.start() # will read [0] as t1 will sleep for 0.2 and this time the t2 will run

# resource competition between threads
a = 0
b = 1000000
def sum1():
    for j in range(b):
        global a
        a += 1
    print(f"sum1: {a}\n", end="")

def sum2():
    for j in range(b):
        global a
        a += 1
    print(f"sum2: {a}\n", end="")

t1 = Thread(target=sum1)
t2 = Thread(target=sum2)
# both will output incorrect number
# as t1 is already started, but t2 is later started when t1 is not finished
t1.start()
t2.start()

# Resolve resource competition between thread
# Synchronous behind this idea -> ensure thread is processed in order
# 1) Thread waiting (using join())
# 2) Mutual exclusion: ensure multithreading will not cause error in resource competition
#  it ensures only one thread is using this resource at the time
# -> basically, when one thread wants to change a shared resource, lock the resource
# -> then other threads cannot modify it until the resource is released
from threading import Lock
c = 0
d = 1000000

lock = Lock()
def s1():
    lock.acquire() # lock
    for j in range(d):
        global c
        c += 1
    print(f"s1: {c}\n", end="")
    lock.release() # release

def s2():
    lock.acquire()
    for j in range(d):
        global c
        c += 1
    print(f"s2: {c}\n", end="")
    lock.release()
t1 = Thread(target=s1)
t2 = Thread(target=s2)
t1.start()
t2.start()