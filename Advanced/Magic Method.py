# Magic Method: refers to all __funcName__ functions
# can be automatically called if certain situation is met

# __doc__ -> describes the comments of the class
class A:
    """this is class information"""
    pass

print(A.__doc__)

# __module__ -> returns which module this class belongs to
class B:
    def __init__(self):
        self.name = "Hello"
print(B.__module__)

# __class__ -> returns the class of the object
b = B()
print(b.__class__)
print(B.__class__) # returns 'type'

# __call__() -> allows the object to use () to call this method
class C:
    num = 1

    def __call__(self, *args, **kwargs):
        print("call")

c1 = C()
c1() # run the __call__ method
C()() # run the __call__ method

# __dict__ -> returns the properties of the class
print(C.__dict__) # returns a dictionary, only has the properties included in class
print(dir(C)) # returns a list, including all properties of class

# __repr__() -> outputs for programmer to debug
class Human:
    def __repr__(self): # for programmer, if no __str__ is defined, __str__ will also use this
        return "hi"

    def __str__(self): # for user
        return "love"

h1 = Human()
print(h1) # if not using __repr__, will return the reference of this object
print(str(h1))
print(repr(h1))

# __getitem__(), __setitem__(), __delitem__()
class T:
    def __init__(self, dictionary):
        self.d = dictionary

    def getD(self):
        return self.d

    # enable object to behave like sequence or containers
    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        self.d[key] = value

    def __delitem__(self, key):
        del self.d[key]

t = T({"name" : "Jack", "age" : 20})
print(t["name"])
t["name"] = "Lucy"
del t["age"]
print(t.getD())