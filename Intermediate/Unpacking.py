# Unpacking: the process of extracting values from a sequence and assigning them to multiple variables

def test():
    a = 10
    b = 2
    c = 30
    return a, b, c
print(test())
a, b, c = test()
print(a, b, c)

# tuple unpacking
t = (1, 2, 3 ,4)
a, *c, b = t # *c will be a list containing several elements
print(a, c, b)

# list unpacking
a, *b = [1, 2, 3]
print(a, b)

# dict unpacking
d = {"name" : "Jack", "age" : 20}
a, b  = d
print(a, b) # values in a, b are keys (no values will be obtained)