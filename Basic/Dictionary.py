# dictionary or map has keys and values
# each key(unique) corresponds to a value
# Note: data in dictionary has no order

# emtpy dictionary
d = {}

dict1 = {
    "name" : "Jack",
    "age" : 20,
    "year" : 2003,
    "name" : "Lucy" # will overwrite the value of name
}
print(dict1)

# change value of specified key
dict1["name"] = "Max"
print(dict1)

# add new element
dict1["num"] = 1
print(dict1)
# Note: with key, if no such key, add this key and value, if already exists, change the value of key

# remove specified kay
del dict1["num"]
print(dict1)

# search using key
print(dict1['name'])

# keys() returns all keys
print(dict1.keys())

# values() returns all values
print(dict1.values())

# items() returns collections of tuples containing both keys and values
print(dict1.items())

# traverse
for key, value in dict1.items():
    print("{} : {}".format(key, value), end=" ")

# dictionary comprehension
dict2 = {i : i * 2 for i in range(5)}
print()
print(dict2)