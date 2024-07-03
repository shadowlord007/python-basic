########## Update Tuple in Python ################

thistuple = ("apple", "banana")
print(thistuple)

# Tuples are unchangeable, meaning that you cannot 
# change, add, or remove items once the tuple is created.
# But there are some workarounds.


#we can convert the tuple into a list, change the list, 
# and convert the list back into a tuple.

thistuple = ("apple", "banana", "orange", "cherry")
print(thistuple)
thislist = list(thistuple)
print(thislist)
# now we can use list methods here and then convert back into tuple
thislist[2] = "kiwi"
# here we replace the orange with kiwi and save it back to tuple
thistuple = tuple(thislist)
print(thistuple)

# we can also use append() method of list
thistuple = ("apple", "banana", "orange", "cherry")
print(thistuple)
thislist = list(thistuple)
print(thislist)
thislist.append("strawberry")
print(thislist)
# now we can turn it back into tuple
thistuple = tuple(thislist)
print(thistuple)

# we can also use remove method of list
thistuple = ("apple", "banana", "orange", "cherry")
print(thistuple)
thislist = list(thistuple)
print(thislist)
thislist.remove("banana")
print(thislist)
# now we can turn it back into tuple
thistuple = tuple(thislist)
print(thistuple)


# we can also the delete tuple completely
# del keyword
# we can also use append() method of list
thistuple = ("apple", "banana", "orange", "cherry")
print(thistuple)
del thistuple
# now this will give error since we have delete the tuple
# print(thistuple)