import time
from multiprocessing import Process, Queue
# q = Queue(3) # q capacity is set to 3
# q.put("message 1")
# q.put("message 2")
# print(q.full()) # check whether queue is full
# print(q.get())
# print(q.qsize())
# q.put("message 3")
# q.put("message 4")
# try:
#     q.put("message 5", True, 2) # block is True means that if queue is full, then wait.
#     # timeout is the time to wait. If not in, throw exception
# except Exception as e:
#     print("Not in")

# Communication between processes using Queue in multiprocessing
# Note: this specific Queue allows resource sharing for processes
l1 = [1, 2, 3, 4]
def write(q1):
    for i in l1:
        q1.put(i)
        time.sleep(0.1)

def read(q2):
    while not q2.empty():
        info = q2.get()
        print(f"Read {info}")

if __name__ == '__main__':
    q1 = Queue()
    p1 = Process(target=write, args=(q1,))
    p2 = Process(target=read, args=(q1,))
    p1.start()
    p1.join() # if no interrupting, p2 will start and will only have read 1 output as p1 is not finished
    p2.start()
    p2.join()

# Process pool -> prepare some processes in a pool first, if there is a task, assign one process to this task
# After finishing, put the process back to the pool

# Synchronous: After assigning a process, it will wait the process finish this task and then run the next code
# As mentioned before, it is in order
# Asynchronous: After assigning a process, it will not wait the process finish, and it will continue run the code
# it saves time

# Asynchronous
from multiprocessing import Pool
def learn(n):
    print("Learning")
    time.sleep(2)
    return n ** 2

if __name__ == '__main__':
    p = Pool(3) # pool contains 3 processes
    l1 = []
    for i in range(6):
        result = p.apply_async(learn, args=(i,)) # apply asynchronous on task
        l1.append(result)
    p.close() # close process pool, then it will no more accept any task
    p.join() # wait until p finished, must apply after pool is closed; otherwise keep waiting

    for j in l1:
        print(j.get()) # need to use get() to obtain result

    # Synchronous
    # Note: much slower than asynchronous as it needs to wait for previous process to finish
    p = Pool(3)
    l1 = []
    for i in range(6):
        result = p.apply(learn, args=(i,))  # apply asynchronous on task
        l1.append(result)
    p.close()  # close process pool, then it will no more accept any task
    p.join()  # wait until p finished, must apply after pool is closed; otherwise keep waiting

    print(l1)

# Communication within process pool
from multiprocessing import Manager
def rd(q):
    for j in range(q.qsize()):
        print("Value get: ", q.get())

def wd(q):
    for j in "123":
        q.put(j)

if __name__ == '__main__':
    q = Manager().Queue()
    p = Pool()

    p.apply_async(wd, args=(q,))
    p.apply_async(rd, args=(q,))
    p.close()
    p.join()