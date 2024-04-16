# encode: convert string to byte literal
a = "hello"
print(type(a))
b = b'Hello' # b indicates the byte literal
print(type(b))

c = a.encode() # encode a to byte literal
print(c)
print(type(c))

# decode: convert byte literal back to string
print(c.decode())

# slicing
name = "Hello world"
print(name[0:6]) # [0: 6) inclusive to exclusive
print(name[0:8:2]) # [0: 8) with step 2
print(name[:]) # print the entire string
print(name[-1:2:-1]) # negative sign in step means starting from end, -1 is the starting end index
print(name[0:20]) # slicing can be out of bound
print(name[2:5:-1]) # this will output nothing as step indicates starting from end while 2:5 indicates from start\

# find(str, start index, end index) return the first index of occurrence of str in a string, otherwise return -1
# [start index, end index)
print(name.find('l'))
print(name.find("world", 6, 11))

# index(str, start index, end index) similar to find() but will throw an exception if not in string
print(name.index('l'))

# count(str, start index, end index) return the number of times the str occurs in string
print(name.count('l'))

# replace(old string, new string, number of times) replace old string with new string
print(name.replace('l', 'a', 2)) # first two
print(name.replace('l', 'a')) # replace all

# split(str, number of times) split the string at str
a = "he,llo, w,ol,d,"
print(a.split(',')) # return a list
print(a.split(' '))

# title() capitalizes the first char of each word
a = "hello, world"
print(a.title())

# join
print('*'.join(a)) # insert * after each char (including space)

# lstrip() # delete the space on the left, similarly rstrip() removes the space on the right
a = " jack"
print(a.lstrip())