# open: open the file and return the object of the file
f = open("D:/Pycharm/Advanced/File/hello.txt")

# read: read the content, will assign the file pointer to the end of file
text = f.read()
print(text)

# write: write content into the file

# close: close the file
f.close()

# property of file object
print(f.name) # name of file (path of file)
print(f.mode) # file opened in which mode
print(f.closed) # check file is closed or not

# Mode of file opening
# r: only read the file, pointer at the beginning, this is default mode
# w: only write the file, if file already exists, then overwrite, else create the file
# a: only append the file, if file already exists, pointer at the end and new content will be added after this
# else create the file
# rb, wb, ab are opening the file in binary format, others are the same as above
# r+, w+, a+ are opening the file in both read and write mode, others the same

# r
f = open("D:/Pycharm/Advanced/File/hello.txt", 'r')
s = f.read(10) # only read first 10 char
print(s)
f.close()

# w
f = open("D:/Pycharm/Advanced/File/hello.txt", 'w')
f.write("Welcome to my world!")
f.close()

# a
f = open("D:/Pycharm/Advanced/File/hello.txt", 'a')
f.write("What?")
f.close()

# Note: sometimes file opening may cause IOError, thus better with try
try:
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

# Or we can use keyword 'with'
# Note: by using 'with', the file will be automatically be closed after using the file
with open("D:/Pycharm/Advanced/File/hello.txt", 'r') as f:
    print(f.read())
print(f.closed)

# Note: above file being read are all UTF-8 type
# To open other file type, using encoding
f = open("D:/Pycharm/Advanced/File/apple.txt", "r", encoding="utf-16 be")
print(f.read())
f.close()

# rb
f = open("D:/Pycharm/Advanced/File/apple.txt", "rb")
print(f.read().decode("utf-16 be"))
f.close()

# wb
# f = open("D:/Pycharm/Advanced/File/apple.txt", "wb")
# f.write("Hello".encode()) # need to encode the string to binary before write
# f.close()

# tell() -> returns the current file pointer in the file
# seek(offset, from) change the filer pointer in the file
# from indicates the position of starting char
f = open("D:/Pycharm/Advanced/File/hello.txt", 'r')
text = f.read(10)
print(text)
position = f.tell()
print(position) # return 10
f.seek(0, 0) # reposition the file pointer
print(f.read(10))
print(f.read())
f.close()

# copy the file
filename = input("Enter your filename in terms of path: ")
index = filename.rfind('.')
newFilename = filename[:index] + "Copy" + filename[index:]

f1 = open(filename, 'r')
text = f1.read()
f1.close()
f2 = open(newFilename, 'w')
f2.write(text)
f2.close()