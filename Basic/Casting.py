# Python 3: 6 standard data type
# Number: int, float, bool, complex
# String: str()
# List: list()
# Tuple: tuple()
# Set: set()
# Dict: dict()


# str()
a = 5
print(type(a))
b = str(a)
print(type(b))

# dict()
a = ['a1', 'a2', 'a3', 'a4']
b = ['b1', 'b2', 'b3']
d = zip(a, b) # use zip first, then dict()
print(d) # return the address of the d
print(dict(d)) # length will be the one with shorter length