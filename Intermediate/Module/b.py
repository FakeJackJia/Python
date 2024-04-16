# import a
# a.func()

from a import func # import specific
func() # output a

# from a import *  -> import all content from a
# cannot do from a import b.c
# but can do from a.d import e


#.py
#1. Script
# __name__=='__main__' -> indicates the code is running in the current file
#2. Module: import to other .py files
# if imported as module, __name__==name of module (no postfix)

if __name__=='__main__': # indicates that current .py is not used as a module
    print("hello")