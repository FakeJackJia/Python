# reference transmission
a = 10
b = 10
print(id(a)) # check the address of a
print(id(b)) # check the address of b
# Note: when two variables have the same value, they use the same address

a = 10
b = a
print(a, id(a)) # similarly, with same value, same address
print(b, id(b))
a = 4
print(a, id(a)) # different value, different address
print(b, id(b))

a = [1, 2, 3, 4]
print(id(a))
b = a # b references a
print(id(b))

# copy
import copy
a = [1, 2, 3, 4]
b = copy.copy(a)
print(a, id(a))
print(b, id(b)) # different address

# deep copy -> means if change the copy, the origin will not be changed
# both the object and the elements inside the object are copied
print("Deep copy")
import copy
a = [1, 2, 3, [5, 6, 7]]
a_deep = copy.deepcopy(a)
print(a, id(a))
print(a_deep, id(a_deep))

a[0] = 3 # a_deep will not change
a[3][0] = 10 # a_deep will not change
print(a, id(a))
print(a_deep, id(a_deep))

# shallow copy -> one level deep
# only copies the elemenst while copied objects inside the object is a reference to the origin
print("Shallow copy")
a = [1, 2, 3, [5, 6, 7]]
a_shallow = copy.copy(a)
print(a, id(a))
print(a_shallow, id(a_shallow))

a[0] = 3 # a_shallow won't change
a[3][0] = 10 # a_shallow will change
print(a, id(a))
print(a_shallow, id(a_shallow))

# reference
print("reference")
a = [1, 2, 3, [5, 6, 7]]
b = a # both a and b reference to the same data
print(a, id(a))
print(b, id(b))

a[0] = 3
a[3][0] = 10 # both change
print(a, id(a))
print(b, id(b))