# Concurrency: perform tasks via interleaving operation of processes (not actually simultaneously)
# -> it uses one single processing unit
# Parallelism: perform tasks simultaneously, by having several processing units dealing with each task at the same time
import threading
# Process vs Thread
# Process: the program under action (the smallest unit of resource allocation, one process per core)
# Thread: the smallest unit of instructions processed by the CPU
# Every process has a thread, no process -> no threads
# Can have multiple threads in process
# And the thread created by programmer is a sub thread

# Single thread
import time
t1 = time.time()
def speak(name):
    print("Welcome", name)
    time.sleep(1)

for i in range(4):
    speak("Jack")

t2 = time.time()
print("Time: ", t2 - t1)

# Multithreading: ability of a processor to execute multiple threads concurrently (not simultaneously!!)
from threading import Thread
t1 = time.time()
def speak(name):
    print("Welcome", name)
    time.sleep(1)

for i in range(4):
    # create thread
    t = Thread(target=speak, args=("Jack",))
    t.start() # start thread

t2 = time.time()
print("Time: ", t2 - t1)

# More example on Multithreaing
def fun1():
    print("f1")
    time.sleep(2)
    print("end f1")

def fun2():
    print("f2")
    time.sleep(2)
    print("end f2")

f1 = Thread(target=fun1)
f2 = Thread(target=fun2)

# Daemon Thread does not block the main thread, if main thread ends, they also end
f1.setDaemon(True)
f2.setDaemon(True)

f1.start()
f2.start()

# join() is used to interrupt the main thread -> main thread needs to wait until these sub threads end
f1.join() # this will first end
f2.join() # this will second end

# change name of thread
f1.setName("Thread 1")
f2.setName("Thread 2")

print(f1.getName(), f2.getName())

print("This is main thread")
# if not interrupting main thread, will not output "end f1" and "end f2" as main thread is ended