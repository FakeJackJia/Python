# Exception handling
# with no specifying error
try:
    print(a)
except:
    print("Error")

# specify error
try:
    print(b)
except NameError as e: # catch exception as name error, and set the error as e
    print(e)

# catch any exception
try:
    print(a)
except Exception as e:
    print(e)

# catch several specifed error
try:
    print(a)
except NameError as e:
    print(e)
except KeyError as e:
    print(e)

# try except else
d = {"age" : 2}
try:
    print(d["age"])
except Exception as e:
    print(e)
else: # only run if except does not run
    print("No error")

# try except finally
try:
    print(a)
except Exception as e:
    print(e)
finally: # will run no matter whether there are exceptions
    print("Finally")

# Full Example
try:
    n = int(input("Enter a number: "))
    print(10 / n)
except Exception as e:
    print(e)
else:
    print("Will output if no exception")
finally:
    print("will run no matter what")

# raise exception actively
def func():
    raise Exception("Error")

try:
    func()
except Exception as e:
    print(e)