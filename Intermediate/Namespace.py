# In Python, order of looking variables
# local -> global -> built in

# global
# Immutable variable
print("Immutable global variable")
a = 100 # global variable

def func1():
    a = 200 # this a is local
    print(a) # 200, won't change global a

def func2():
    print(a) # 100
func1()
func2()


def func3():
    global a # set a in function as global variable
    a = 200 # will change global a
    print(a)

def func4():
    print(a)
func3()
func4()


#a = 1
# def fun():
#     print(a) # this a is local, so error occurred
#     a = 2
# fun()

# Mutable variable
print("Mutable global variable")
l1 = [1, 2, 3, 4] # global variable

def func5():
    l1[0] = 5 # can use without using global
    print(l1)
func5()

# nonlocal: cannot change global variable
# instead, it uses parent's variable and can modify the variable in parent
a = 10
def funa():
    a = 1
    def funb():
        nonlocal a
        print(a)
        a = 2
    funb()
    print(a)
funa()
print(a)