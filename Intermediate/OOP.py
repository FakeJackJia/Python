# class: name is capitalized
class Hero(object): # object is parent class of all classes, can be removed
    name = "Jack" # attribute

    # this is a method
    def info(self): # self -> indicates the object itself, can be other name
        print(self)

# initialize an object
a = Hero()
a.info()
print(a.name)
print(Hero.__dict__) # check the properties of the class

# change member of a class
Hero.name = "Fake"
print(a.name) # will change the name

del Hero.name # delete this member
try:
    print(a.name)
except Exception as e:
    print(e)

Hero.walk = "walk" # add new member
print(Hero.walk)
# Note: if member already exists, then change it, else add it

# change member of an object
a.name = "Apple"
a.hp = 100

print(a.hp, a.name)

# Attribute
class A:
    num = 0 # attribute of class
    def __init__(self, name):
        self.name = name # attribute of object

    def test(self):
        print(f"my nam is {self.name}")

    def test1(self, age):
        self.age = age
b = A("Jack")
print(b.name)
#print(B.name) cannot work as it is attribute of object
b.test()

#print(b.age) will cause error
b.test1(1) # need to call test1 first to initialize age
print(b.age)

# Constructor: when creating object, data members is initialized
# __init__, will automatically run after creating object (no return value)
# Destructor: it is called when all references to the object have been deleted (not used a lot, as python has garbage collector)
# __del__, will automatically run after deleting object (no parameter, only one destructor)
class Student:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def __del__(self): # destructor
        print("Destroyed")

    # __str__() method -> when printing object, output self-defined content
    # must return a string
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

jack = Student("Jack", 20)
print(jack.name)
print(jack)
del jack # manually delete object, will call destructor, if not manually, call at the end of program