# Immutable: original data cannot be changed, if updated, need to allocate new memory for the resulted value
# e.g. int, bool, float, complex, str, tuple
print("Immutable")
i = 73
print(i, id(i))
i += 2 # it will not change the value of 73, instead, it will create another object with resulted value
print(i, id(i))


s1 = "abc"
print(id(s1))
s1 = ""
print(id(s1))

a = True
print(id(a))
a = False
print(id(a)) # different address
a = True
print(id(a)) # same address as the original one, as same value

# Mutable: data can be changed, address will not be changed
# e.g. dict, list, set
print("Mutable")
l1 = [5, 9]
print(id(l1))
l1 += [54]
print(id(l1)) # address won't be changed