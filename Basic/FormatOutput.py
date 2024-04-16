# Format output: print(template % variable)
name = "Jack"
age = 21

# %s for string and %d for decimal
print("My name is %s, and my age is %d" % (name, age))

# %f for float
a = 1.23456
print("%.2f" % a) # .2f keep 2 decimals

# Instead of using above complicated one, use format()
print("{}, {}".format(name, age)) # each variable will be matched up with corresponding {}

# format with number eg. {1}, {2}
print("{0}, {1}, {0}".format(name, age)) # starting with 0

# format with parameter
print("{name}, {age}".format(name=name, age=age))

# f'{expression}'
print(f"name:{name}, age:{age}")