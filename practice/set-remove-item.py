########## remove item from Sets in Python ################

thisset = {"apple", "banana", "cherry", "mango"}
print(thisset)

# we can remove an item in a set, 
# use the remove(), method 

thisset = {"apple", "banana", "cherry", "melon"}
print(thisset)
# if the item is not exist the rmemove method will raise an error
thisset.remove("apple")
print(thisset)

# and the discard() method.
thisset = {"apple", "banana", "cherry", "melon"}
print(thisset)

thisset.discard("banana")
print(thisset)


# we can also use pop() method to remove 
# but the pop method will remove the random value so we don't know
# which one removed

thisset = {"apple", "banana", "cherry"}
popItem = thisset.pop()
print(popItem)
print(thisset)

# we can use clear() method
# this onw will remove the content of set
thisset = {"apple", "banana", "cherry", "melon"}
print(thisset)
thisset.clear()
print(thisset)

# we can alos use del keyword
# this will also delete the set initilization
thisset = {"apple", "banana", "cherry", "melon"}
print(thisset)

del thisset
# now we delete the set this will raise an error
# print(thisset)