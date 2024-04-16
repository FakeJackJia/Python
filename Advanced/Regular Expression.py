# Regular Expression
# used to check whether a string is matched with certain pattern

import re
# if not match, return None, if match return the result of matching pattern
# Note: match() starts at the beginning of the string
res = re.match("s", "study")
print(res.group()) # return the result

# matching single char (any char except \n)
print(re.match('.', 'a').group())
print(re.match('t.o', 'too').group())

# [] -> any char in [] is matched
print(re.match('[hH]', "hello").group()) # return h

# [0-9] -> matching 0 to 9
print(re.match('[0-9]', '123').group()) # return 1

# matching 0 to 9 except 4
print(re.match('[0-35-9]', '3').group())

# using \d to match number
print(re.match('\d', '32').group())

# using \s to match space
print(re.match('\ss', ' s').group())

# * -> repeat 0 to any times
print(re.match('[A-Z][a-z]*', 'SxcS').group())

# + -> repeat at least 1 time
print(re.match('[a-zA-Z]+python', 'AnyWhatpython').group())

# ? -> repeat at most 1 time
print(re.match('[1-9]?[0-9]', '213').group())

# {m} -> repeat m times
print(re.match('[0-9]{6}', '1234567').group())

# {m, n} -> repeat at least m and at most n times
print(re.match('[a-zA-Z0-9]{3,9}', 'Love2024').group())

# ^ -> start with certain string
print(re.match('^ab', 'abc').group())
print(re.match('[^0-9]', 'z').group()) # if written in [], it indicates 'Not'

# $ -> ends with certain string
print(re.match('[1-9]?\d$', '10').group())

# | -> or
print(re.match('[1-9]?\d$|123', '123').group())

# () -> set the char in () as a group
print(re.match('1\d{10}@(139|qq).com', '12345678911@139.com').group())
print(re.match('(ab)*', 'ababab').group())

# \\num -> reference group num (indicates to look the same pattern in that group)
print(re.match('(139|qq)--\\1', '139--139').group())

# (?P<name>) -> set the name for the group
# (?P=name) -> use the group with name
print(re.match('(?P<n1>139|qq)--(?P=n1)', '139--139').group())

# search() -> scan the entire string and return the first match
print(re.search('\d+', '123d23').group())

# findall() -> return a list of matched string in a given string
print(re.findall('\d+', '123d23f1')) # no need to use group() to output result

# sub() -> replace the matched string in a given string with the specified string
print(re.sub('\d', '123', 'I study for 2 hours in 2 days'))
# can set a number of times to replace
print(re.sub('\d', '1', '3d3we3',2))

text = ("<p> data science, machine learning, .... </p> "
        "<div> play and fun </div>")
print(re.sub('<[^>]*>', '', text))

# split() -> split the string by a given criteria and return a list
print(re.split(':', 'ab:cd:c'))
print(re.split('[: ]', ' a b:c d', 3))

# greedy matching: when matching the pattern, include as much as possible
# non-greedy matching: when matching the pattern, include as little as possible
print(re.match('ab*', 'abbbc').group()) # greedy
print(re.match('ab*?', 'abbbc').group()) # non-greedy

# Raw string: treat escape character \ as literal character
print('hello \\n world') # if not raw string, need to use \\ to represent \
print(r'hello \n world')
# Note: \\\\ represents \ in regular expression
print(re.match('\\\\', '\d').group())
print(re.match(r'\\', '\\').group())