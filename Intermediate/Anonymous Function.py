# Anonymous function: a function definition that is not bound to an identifier
# function name: lambda parameter : return value

# Example 1
func1 = lambda a, b : a + b
print(func1(1, 2))

# Example 2
s = "hello"
func2 = lambda x : [x[0], x[1]]
print(func2(s))

# if else
a = 10
b = 3
print(a) if a > b else print(b) # conditional operator