# __new__(): when creating object, this is the first one to be called (not __int__())
# 1) allocates space for object
# 2) returns reference of object and this return leads to call of __init__()
# if no return value, then no call of __init__()
# if return not returning the reference of object, __init__() will not be called
class Person:
    def __new__(cls, *args, **kwargs):
        print("new method")

    def __init__(self):
        print("init method")
p = Person() # no call of __init__()

class Person1:
    def __new__(cls, *args, **kwargs):
        print("new method")
        #return object.__new__(cls) same as below
        return super().__new__(cls) # call parent class's __new__ method, return object of current class

    def __init__(self):
        print("init method")
p1 = Person1() # __init__() is called

# Singleton: a special class, can only create one object of this class
# Singleton pattern: for all classes, the objects of the same class reference to the same address
# can save space

# Essence behind singleton pattern:
# 1) check whether this object exists or not
# 2) if exists, return this object, if not, create this object

# using __new__()
class People:
    ins = None # ins used to reference to the object

    def __new__(cls, *args, **kwargs):
        if cls.ins is None: # only creates new objects if it is none
            cls.ins = super().__new__(cls)

        return cls.ins
t1 = People()
t2 = People()
print(id(t1), id(t2)) # same address

# using classmethod
class Sing:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            Sing.instance = super().__new__(cls)

        return cls.instance
a = Sing.get_instance()
b = Sing.get_instance()
print(id(a), id(b)) # same address

# using decorator
def outer(cls):
    _ins = {}
    def inner():
        if cls not in _ins:
            _ins[cls] = cls()

        return _ins[cls]
    return inner

@outer
class A:
    a = 1

a1 = A()
a2 = A()
print(id(a1), id(a2)) # same address

# using import
# Note: module in python is natural singleton mode
from Singleton import Test
from Singleton import Test # Note: only output one address for A

# using hasattr(object, string) -> used to check whether the object has the specified property
class B:
    b = 2
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "ins"):
            cls.ins = super().__new__(cls)

        return cls.ins

    def __init__(self, name):
        self.name = name

    def test(self):
        print("test")

print(hasattr(B("a"), "b")) # return true as b is attribute of class B
print(hasattr(B("b"), "test")) # return true as test is method of class B
b1 = B("A")
b2 = B("B")
print(b1.name, b2.name) # both output B as both references the same object
print(id(b1), id(b2)) # same address