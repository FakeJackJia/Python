# User input
# input() will treat all user input as string
name = input("Please enter your name: ")
print(name)

num = input("Please enter a number: ")
print(type(num))

# need to cast the input to int to limit the input to int
num = int(input("Please enter an integer: "))
print(type(num))

# eval(): if the expression is a legal Python statement, it will be executed.
num = eval(input("Please enter: "))
print(type(num))