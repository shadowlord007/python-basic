########## Sets in Python ################


#Sets are written with curly brackets.
thisset = {"apple", "banana", "orange"}
print(thisset)

# serts also can be writter with set() constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# length of a set
thisset = {"apple", "banana", "orange"}

print(thisset)
print(len(thisset))

# set can be of any data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

# set can contain different data types:

thisset = {"abc", 34, True, 40, "male"}
print(thisset)
print(type(thisset))