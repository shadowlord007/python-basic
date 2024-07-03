########## Joins Sets in Python ################

# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first 
# set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# using union()
set1 = {"apple", "banana", "cherry", "mango"}
print(set1)
set2 = {1, 2, 3, 4, 5 }
print(set2)

set3 = set1.union(set2)
print(set3)

# using | same as union
set1 = {"apple", "banana", "cherry", "mango"}
print(set1)
set2 = {1, 2, 3, 4, 5 }
print(set2)

set3 = set1 | set2
print(set3)


# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, 
# separated by commas:

set1 = {"apple", "banana", "cherry", "mango"}
print(set1)
set2 = {1, 2, 3, 4, 5 }
print(set2)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# using | same as union for multiple

set1 = {"apple", "banana", "cherry", "mango"}
print(set1)
set2 = {1, 2, 3, 4, 5 }
print(set2)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


#The union() method allows you to join a set with other data types, 
# like lists or tuples.

#The result will be a set.
set1 = {"apple", "banana", "cherry", "mango"}
print(set1)
tuple1 = (1, 2, 3, 4, 5 )
print(tuple1)

myset = set1.union(tuple1)
print(myset)


# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
set1 = {"apple", "banana" , "cherry"}
print(set1)
set2 = {1, 2, 3}
print(set2)
set1.update(set2)
print(set1)



#Keep ONLY the duplicates
#The intersection() method will return a new set, 
# that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# use & same as intersection() 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)


# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set3)

#Join sets that contains the values True, False, 1, and 0, 
# and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
print(set1)
set2 = {False, "google", 1, "apple", 2, True}
print(set2)
set3 = set1.intersection(set2)

print(set3)



#The difference() method will return a new set that will contain 
# only the items from the first set that are not present in 
# the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# we can use (-) as as difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2

print(set3)

#The difference_update() method will also keep the items from the 
# first set that are not in the other set, but it will change the 
# original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


# The symmetric_difference() method will keep only the elements 
# that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# we can use (^) this same as symmetric_difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)


# The symmetric_difference_update() method will also keep all but 
# the duplicates, but it will change the original set instead of 
# returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

