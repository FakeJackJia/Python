# package: folder that contains _init_.py
# used to manage different modules
from package import t1, t2 # if first import, run first e.g. t1 runs before t2
print("_init_.py")

__all__ = ['t1', 't2'] # it defines what to be imported if call import *