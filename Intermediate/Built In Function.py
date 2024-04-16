# zip(), zip corresponding element in the object as a tuple
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))

c = (4, 5, 6, 7)
for i in zip(a, b, c):
    print(i)

# map(function, iterable)
# apply function for each element in iterable object
l = [1, 2, 3, 4]
print(list(map(lambda x : x**2, l)))

# reduce(function, iterable)
""" At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result 
and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container. """
from functools import reduce
print(reduce(lambda x, y : x + y, [1, 2, 3, 4]))

# enumerate(iterable) -> collection of (index, element)
l = [1, 2, 3, 4]
for i, j in enumerate(l):
    print(i, j)