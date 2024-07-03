########## Add item in Sets in Python ################

thisset = {"apple", "banana", "cherry", "mango"}
print(thisset)

# to add the item in set we will use
# add() method
thisset.add("melon")
print(thisset)

# when trying to add other set item into 1st set 
# update() method

set1 = {"apple", "banana", "cherry", "mango"}
print(set1)
set2 = {"pineapple", "mango", "papaya"}
print(set2)

set1.update(set2)
print(set1)

# we can also add the list, tuple, dictionary into the set
thisset = {"apple", "banana", "cherry"}
print(thisset)
thislist = ["pineapple", "mango", "papaya"]
print(thislist)

thisset.update(thislist)
print(thisset)
