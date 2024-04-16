# generator is a special iterator
# a function that returns an iterator that produces a sequence of values when iterated over.
# generators are useful when we want to produce a large sequence of values
# and we don't want to store all of them in memory at once.
# use keyword 'yield'

from collections.abc import Iterator, Generator

def func():
    yield 1 # returns a generator, only yield in def creates a generator
    return "Error" # not as a return value, but an illustration of StopIteration
t = func()
print(isinstance(t, Iterator))
print(next(t))
try:
    print(next(t))
except Exception as e:
    print(e) # output Error as specified as above

def func1():
    yield 1
    yield 2

for i in func1():
    print(i)

# Example use of generator
def use(fname):
    with open(fname) as f:
        for i in f:
            yield i

gen = use("D:/Pycharm/Advanced/File/generator.txt")
for line in gen:
    print(line, end="")

print()
# create generator outside function
list1 = (i * 2 for i in range(3))
print(isinstance(list1, Generator))
print(next(list1))
print(next(list1))

# Advantage of generator
# 1) only return one result at a time, will not calculate all results at once, useful a large batch of data
# 2) save memory space

# difference between yield and return
# return will end the process of function
# yield will turn the function into a generator, will not end the function until StopIterator occurs