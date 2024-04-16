# Set: no repeating elements, unordered
s1 = {10, 20, 30}
print(type(s1))

s2 = set("hello")
print(s2)
print(type(s2))

# define empty set
s3 = set()
print(s3)

# add new element
s1.add(1) # can only add single element
s1.add(10) # automatic remove repeating elements
print(s1)

# update(element) with element that is iterable
s1.update([0, 1])
print(s1)

s1.update({100 : 2}) # only key in dict will be added
print(s1)

# remove(element) remove specified element
s1.remove(0)
print(s1)

# discard(element) remove specified element
s1.discard(100)
s1.discard(100) # remove element not in set will not cause error
print(s1)

# pop() will randomly remove element and return that element
print(s1.pop())
print(s1)

# intersection between set
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print(x & y)

# union between set
print(x | y)