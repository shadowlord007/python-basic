############ List Copy ###########

#You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, and changes
# made in list1 will automatically also be made in list2.

# copy() method
# 1st way
thislist = ["apple", "orange", "banana", "mango", "kiwi"]
print(thislist)
newlist = thislist.copy()
print(newlist)

# sorting numeric value

thislist = [100, 20, 50, 19, 37, 60]
print(thislist)
newlist = thislist.copy()
print(newlist)


# 2nd way
thislist = ["apple", "orange", "banana", "mango", "kiwi"]
print(thislist)
newlist = list(thislist)
print(newlist)

# sorting numeric value

thislist = [100, 20, 50, 19, 37, 60]
print(thislist)
newlist = list(thislist)
print(newlist)



