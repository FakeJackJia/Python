# Tuple: elements cannot be altered or deleted -> increase security
num_list = (10, 20, "1")
print(num_list)

# if define tuple with only one element, add , after
t1 = (2)
print(type(t1))
t2 = (2,)
print(type(t2))

# index(element) returns the index of the element, if not throw exception
t3 = (2, 3, 1, 0, 9, 1)
print(t3.index(0))

# count(element) returns the number of times element occurs
print(t3.count(1))

# tuple compression
t = (i for i in range(10))
print(t) # returns the address of object
print(tuple(t))