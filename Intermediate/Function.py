#import random
#help(random) # check how function random works
#print(random.__doc__) # similar to above

# function definition
def func():
    a = 10

    return a
func() # return result will not be directly printed
print(func()) # need to use print()

# return several values (several values but as a whole)
def func1():
    return 1, 2, 3 # return multiple values as a tuple by default containing these values
print(func1())

# function with no return, will have a default return None
def func2(x): # x is parameter
    print(x)

print(func2(2)) # None

print("Parameters")
# Positional argument: must pass a value
def funcP(a, b):
    print(a - b)
funcP(1, 2) # pass no. of values matching up with positional argument

# Default argument: if no value passed, then use the default one, if passed, then used the passed one
def funcD(a=1):
    print(a )
funcD()
funcD(3)

# Variadic argument: *args, can pass 0 ~ n values
def funcV(*args):
    print(args)
funcV(1, 2, 3, 4) # if passed more than one value, then it is a tuple

# Keyword argument: **kwargs, key=value(unlike default argument, it is passed as values not in parameters)
def funcK(**kwargs): # treats input as dictionary
    print(kwargs)
funcK(name="jack", age=10)

# Parameters order: Positional Argument, Default argument, Variadic argument, Keyword argument
def funcAll(a, b=10, *c):
    print(a, b, c)
funcAll(1, 2, 3, 4)

# if default after variadic
def funcAll1(a, b=10, *c, d=3):
    print(a, b, c, d)
funcAll1(1, 2, 3, 4, 5, d=5) # need to specify keyword, otherwise, use the default


# nested function
def funa():
    def funb():
        print("b")
    print("a")
    funb()
funa()