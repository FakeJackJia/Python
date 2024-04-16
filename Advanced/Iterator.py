# Iterable object: string, list, tuple, dict, set....
# 1) achieved the method of __iter__()
# 2) __iter__() returns an object of iterator

# isintance(object, Iterable) checks whether it is an iterable object
from collections.abc import Iterable, Iterator
print(isinstance([1, 2, 3], Iterable))
print(isinstance([1, 2, 3], Iterator))
print(isinstance(1, Iterable))

# Iterator starts at the first element in collections, until all elements have been visited
# Iterator has two methods: __iter__() -> creates the iterator, __next__() -> retrieve the next element
# Note: an iterator is also an iterable

# Property of iterator:
# 1) user does not need to care the internal structure
# 2) cannot access a random element in a collection, must be in order
# 3) can only go next but not go back
# 4) after one complete use, iterator will not be worked again -> need to create a new iterator

# Operation behind for loop:
# 1) call __iter__() from the desired object to retrieve iterator
# 2) then call __next__() each time
# 3) until all elements been accessed, then throw StopIteration exception, and for loop will catch it and stop

l1 = [1, 2, 3, 4]
#iterator = l1.__iter__()
iterator = iter(l1) # same as above
print(next(iterator)) # same as iterator.__next__()
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator)) # StopIteration
except Exception as e:
    print(e)

# Use of iterator: can iterate a large dataset, save memory space, not rely on the index
class Person:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        self.n += 1
        return self.n

a = Person()
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
it_a = iter(a)
print(next(it_a))
print(next(it_a))

class P:
    def __iter__(self):
        self.n = 1
        return PIterator(self.n)

class PIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        pass

    def __next__(self):
        self.n += 1
        return self.n

p = P()
print(isinstance(p, Iterable))
print(isinstance(p, Iterator))
it_p = iter(p)
print(isinstance(it_p, Iterator))
print(next(it_p))