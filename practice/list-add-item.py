############ Add list item ###########

thislist = []
print(thislist)

# append() method 
# which only take one parameter what to add
#this will add the item in list at the end of list
thislist.append("apple")
print(thislist)
thislist.append("banana")
print(thislist)

#to insert at specified point in the list we use insert() method
thislist.insert(1, "mango")
print(thislist)


# extend() method 
# which is used if we want to extend our list with another list
# like putting the 2nd list item into the 1st list at the end of list

thislist = ["apple", "banana", "cherry"]
list2 = ["mango", "strawberry", "orange"]

thislist.extend(list2)
print(thislist)

# this extend() method
# can extaend the list with any collection data-type like
#tuple, set, dictionary

thislist = ["apple", "banana", "cherry"]
thistuple = ("mango", "orange")
thislist.extend(thistuple)
print(thislist)