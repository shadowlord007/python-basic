############ Remove list item ###########

thislist = ["apple", "banana", "orange"]
print(thislist)

# remove() method
#this method will remove the specific item from the list

thislist = ["apple", "banana", "orange", "kiwi"]
print(thislist)
thislist.remove("orange")
print(thislist)

## if in the list the specified item occure more the one then
# then the remove() method will remove the 1st instance in the list
thislist = ["apple", "banana", "orange", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)


# pop() method
# we can also use pop() method to remove the specified index form the list
# if we did not specified the index in pop then it will remove the last item from the list

thislist = ["apple", "banana", "orange", "banana", "cherry"]
print(thislist)
thislist.pop(3)
print(thislist)

thislist.pop()
print(thislist)

# del is a keyword
# with del we can also remove the specified index from the list

thislist = ["apple", "orange", "strawberry", "melon"]
print(thislist)
del thislist[2]
print(thislist)

#alos the del keyword can delete the entite list
thislist = ["apple", "orange", "strawberry", "melon"]
print(thislist)
del thislist
# print(thislist) if this print is used then it will cause error since the list id deleted


# clear() method
# this method will also clear the content of the list but the list initailization will still be remain

thislist = ["apple", "banana", "orange"]
print(thislist)
thislist.clear()
print(thislist)