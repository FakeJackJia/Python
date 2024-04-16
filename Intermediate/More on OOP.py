# Encapsulation: involves restricting direct access to some of an object's members,
# providing controlled access via methods.
# private members -> cannot be accessed by object, but can be accessed inside the class
# the child class cannot inherit private members of parent class

# _x is weak private, indicate for internal use, but can be accessed by objects and child class
# __x to define true private attributes and methods
# x_ used only to avoid conflict with keyword embedded in python
class Student:
    def __init__(self, name, age):
        self._name = name # weak private
        self.__age = age # private attribute

    def getName(self):
        return self._name

    def getAge(self): # encapsulation
        return self.__age

    def __sing(self): # private method
        print("Sing")

    def action(self):
        self.__sing() # can be called in another method, object can call this public method to call private

    def updateAge(self, age): # update private attribute by public method
        self.__age = age

jack = Student("Jack", 21)
print(jack._name)
try:
    print(jack.__age)
except Exception as e:
    print(e)
jack.updateAge(32)
print(jack.getAge())
jack.action()

# Inheritance: child class can use members of parent class(except private members)
# format: class childName(parentName):
# Single inheritance: inherited from a single base class
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def sing(self):
        print("sing")

    def dance(self):
        print("dance")

class Jack(Person):
    def jump(self):
        print("jump")

j = Jack("Jack", "M", 20)
j.sing()

class Black(Jack):
    def rap(self):
        print("rap")

b = Black("B", "M", 12)
b.jump() # parent class
b.sing() # parent of parent class
b.rap() # itself
# Note: inheritance can be transferred
# parent -> child(have parent property) -> child of child(have all above property)

# Polymorphism: overrides parent's method (only happens in inheritance)
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{} Eat apple".format(self.name))

class Son(Human):
    def __init__(self, name, age):
        super().__init__(name, age) # call __init__() from parent class

    def eat(self): # overriding parent's method
        print("Eat banana")

    def parentEat(self):
        Human.eat(self) # intrinsically using parent class name to call method
        super().eat() # similar to above, super() indicates the parent of current class

son = Son("Son", 3)
son.eat()
son.parentEat()
# Note: override and overload are different
# override is when two methods have the same name and same parameter
# overload is when two methods have the same name but different parameter

# Multiple Inheritance: a child class can inherit from two or more parent classes
class A:
    def test(self):
        print("A class")

class B:
    def test(self):
        print("B class")

class C(A, B): # inherits A and B class
    pass

c = C()
c.test() # will call method in A if both A and B have test() method
print(C.__mro__) # order of calling method in C
# if parent classes have several members with the same name, will use the first parent class by default
# the above also applies to super()

# Method of class -> can be accessed by class without creating objects
# Note: it can access or modify members of class
# need to use decorator: @classmethod
# Note: the first argument must be class itself, usually cls (represents the name of class)
class People:
    age = 20 # attribute of class

    @classmethod # method of class
    def getAge(cls):
        return cls.age

    @classmethod
    def updateAge(cls, age):
        cls.age = age

    def instance(self):
        print("instance")

p = People()
print(p.getAge()) # object can access class method
print(People.getAge()) # without creating object
People.updateAge(1) # update class attribute
print(People.getAge())
#People.instance() this won't work
People.instance(p) # this will work by passing object as an argument

# static method in class: similar to class method but it does not require any argument
# Note: it cannot access or modify members of the class
# need to use decorator: @staticmethod
class Dog:
    name = "Happy"

    @staticmethod
    def bark():
        print("Hello")

dog = Dog()
dog.bark() # object can access static method
Dog.bark() # without creating object
# Overall, classmethod and staticmethod can be accessed by both class and object
# However, for other methods, in order for class to access, need to pass an object as an argument