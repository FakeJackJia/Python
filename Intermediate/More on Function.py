# Pass by reference: when function receives a mutable object as a parameter, change will be applied
# Pass by value: when function receives an immutable object as a parameter, change will not be applied

# reference of function
def test():
    print("test")
res = test
res()

# Closure:
# 1) a function that is defined in another function
# 2) must reference the variable (non-global variable) in the outer function
# 3) the return value of outer function is the inner function

# why closure?
# 1) allow local information to not be destroyed
# 2) decorator

# Example 1
def outer(m):
    n = 10
    def inner():
        print("Inner ", n + m)

    return inner

outer(2)()

# Example 2
def out(a):
    def inner():
        nonlocal a # indicates it is using variable in out, as inner function cannot change variable in outer when it is immutable
        a += 1
        print(a)
    return inner
out(1)()

# Example 3
def out1(a):
    def inner(b):
        return a * b
    return inner
print(out1(1)(3))

# Decorator is a closure function, modify the behaviour of a function or class.
# 1) need first define decorator function or class
# 2) then define your desired function or class
# 3) then put the decorator to your function (@decorator name)

# Example decorator
def logger(func):
    def wrapper(*args):
        print("calculating {}".format(func.__name__))

        func(*args)
        print("finished")
    return wrapper

@logger # pass function add into the logger function
def add(x, y):
    print("{} + {} = {}".format(x, y, x + y))

add(1, 3)

# Decorator when the desired function with no parameter
def test1(func):
    def inner():
        print("this is inner")
        func()
    return inner

@test1
def t1():
    print("hi")

t1()

# multi nesting
def exam(func):
    def funa(x, y):
        print("{}, {}".format(x, y))
        def inner(a, b):
            print("inner")
            func(a, b)
        return inner
    return funa

@exam
def t2(a, b):
    print(a + b)

t2(3, 4)(5, 6)

# Callback function: when this function is passed as an argument to another function
def callback(m, n):
    if m == 2:
        n()
    else:
        print("not callable")

def one():
    print("one")

callback(2, one)