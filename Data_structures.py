# data structures practice
# list, tuple, set, dictionary, slicing

# list
k = [11, 23, 34, None, 56, 11, 23, 44, 22, None, 56]
print(type(k))
print(k[-1])           # last element
print(k[-2])           # second last element
print(k[2])            # index 2 element
k[2] = 100             # mutable - we can change value
print(k)               # ordered
print(k)               # none accepted many times
print(k)               # duplicate allowed


# tuple
k = (11, 22, 33, None, 11, 94)
print(type(k))
print(k[0])            # first element
print(k[-1])           # last element
print(k[-0])           # same as first element
print(k)               # ordered, duplicate allow, none accepted many times
# k[1] = 100           # immutable - this will give error


# set
s = {11, 22, 33, 11, 22, 33, 43}
print(type(s))
print(s)               # unordered, unique, duplicates removed automatically
# print(s[0])          # not subscriptable - this will give error
# s[0] = 444           # immutable - this will give error


# dictionary
d = {"sri": 100, "bala": 99, "kavin": 88, "parthi": 77, "aakash": 66, "sri": None, "bala": 85}
print(type(d))
print(d)
d["sri"] = 90          # value mutable - update existing value
print(d)
d["kishore"] = 95      # add new record at end
print(d)


# string slicing
num = "pradeepa"
print(num[0])          # first character
print(num[4])          # index 4 character
print(num[-3])         # 3rd from last
print(num[:3])         # first 3 characters
print(num[3:7])        # index 3 to 6
print(num[3:])         # from index 3 to end
print(num[::2])        # every 2nd character
print(num[::-1])       # reverse the string

name = "mouse"
print(name[1:4])       # index 1 to 3
