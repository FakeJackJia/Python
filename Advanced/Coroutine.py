# Coroutine: a smaller unit than thread, and is execution of multiple tasks concurrently within a single thread
# coroutine can be suspended and resumed
# Note: thread and process is controlled by the CPU whereas coroutine is controlled by the programmer

# normally used when there are many IO operations as if let cpu control(using thread), need more space and time

# using greenlet to create coroutine
# it is manually switching coroutines
from greenlet import greenlet
def eat():
    print("Too late")
    g2.switch() # switch to g2
    print("Still want to eat") # when switched back, continues at this point
    g2.switch()

def sleep():
    print("Want to sleep")
    g1.switch()
    print(">_<")

g1 = greenlet(eat) # create coroutine g1
g2 = greenlet(sleep) # create coroutine g2
g1.switch() # using switch() to run the function

# using gevent to create coroutine
# it is automatically switched to other coroutine when encountered time-consuming operation
import gevent
def func(n):
    for i in range(n):
        print(i)
        gevent.sleep(1) # monitering time-consuming

g1 = gevent.spawn(func, 2) # 2 is the parameter passed
g2 = gevent.spawn(func, 2)
g1.join()
g2.join() # note: output two 0s first, then 1

# joinall() is used run all specified coroutine, will also interrupting main thread
gevent.joinall([gevent.spawn(func, 2), gevent.spawn(func, 2)])


# Application of coroutine, thread, process
# 1) if CPU-Bound, use multiprocessing
# 2) if IO-Bound, use thread
# 3) if both, multiprocessing and coroutine