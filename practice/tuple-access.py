########## Access Tuple in Python ################

thistuple = ("apple", "banana")
print(thistuple)

#You can access tuple items by referring to the index 
# number, inside square brackets:

thistuple = ("apple", "banana", "orange")
print(thistuple)
print(thistuple[0])

# we can also use negative index to fet it item in tuple
thistuple = ("apple", "banana", "cherry", "mango")
print(thistuple[-1])

# also we can define the range of index
thistuple = ("apple", "banana", "cherry", "mango", "apple", "banana", "orange")
print(thistuple)

# negetive index range
print(thistuple[-5:-1])
print(thistuple[-5:])
print(thistuple[:-1])

# positive index range
print(thistuple[0:3])
print(thistuple[3:])
print(thistuple[:2])