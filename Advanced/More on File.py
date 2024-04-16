# Operations on folder
import os

# rename(old name, new name) to rename folder
#os.rename("D:/Pycharm/Advanced/File", "D:/Pycharm/Advanced/NewFile")

# create new folder
os.mkdir("D:/Pycharm/Advanced/Test Folder") # error if folder already exists

# remove folder
os.rmdir("D:/Pycharm/Advanced/Test Folder")

# get current directory
print(os.getcwd())

# get the list of current directory
print(os.listdir())

# readline() -> read one line each time
with open("D:/Pycharm/Advanced/File/lines.txt", 'r') as f:
    while True:
        text = f.readline() # note: each line of content has \n at the end
        if not text:
            break
        print(text, end="")

# readlines() -> return a list where each element is each line
print()
f = open("D:/Pycharm/Advanced/File/lines.txt", 'r')
print(f.readlines())
f.close()