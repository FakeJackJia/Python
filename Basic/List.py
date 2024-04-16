# list: can store different types of data
list1 = [1, 2, 3.0, "hi"]
print(list1)

list2 = [1990, 1991, 1992]

# +: concatenate two lists
print(list1 + list2)

# insert(index, element) insert element at index
list2.insert(1, 2000)
print(list2)

# extend() add element at the end but will split the element into individuals
list2.extend(list1)
print(list2)

# append() add element at the end, the element will be treated as whole
list2.append((1, 2))
print(list2)

# change a list of elements in a list using slicing
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums[2:5] = [5, 4, 3]
print(nums)

# special case: insert element(in iterable format) using empty slicing
nums[1:1] = [5, 6, 7] # insert 5, 6, 7 at 1
print(nums)

# del: delete entire list
a = list('hello')
print(a) # ['h', 'e', 'l', 'l', 'o']
del a

# del listname[index]: delete specific element at index
b = [1, 2, 3, 4, 5]
del b[1:3]
print(b)

# pop(index) delete the element at index, by default, delete the last one
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums.pop()
nums.pop(4)
print(nums)

# remove(element) remove specified element
nums = [1, 2, 1, 3, 2, 3, 1]
nums.remove(2) # remove the first 2 encountered
print(nums)

# clear() remove all elements in a list
nums.clear()
print(nums)

# sort() in ascending order
nums = [4, 3, 1, 6, 2, 0]
nums.sort() # reverse=True then descending order
print(nums)
nums.reverse() # reverse the list
print(nums)

# Note: sort() only works for list
# sorted() is more generalize
print(sorted(nums)) # sorted() is not inplace sort but sort() is inplace

# list comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i * 2 for i in nums])

# * duplicate specified times
l = ["hello"]
print(l * 4)

# enumerate() returns (index, element)
for index, num in enumerate(nums):
    print(index, num, end=" ")