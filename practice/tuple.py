########## Tuple in Python ################
# tuple is also a data type in python like list, set, dict,
# but the tuple use for different purpose

thistuple = ("apple", "banana", "orange")
print(thistuple)

# we can also use a tuple() contructor to create the tuple
thistuple = tuple(("apple", "banana"))
print(thistuple)
print(type(thistuple))

#Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# the item in typle are ordered, unchangebale, allow dublicate
# value because it store value on index.

thistuple = ("apple", "banana", "orange", "cherry", "banana")
print(thistuple)

# tuple length
thistuple = ("apple", "banana", "orange", "cherry", "banana")
print(len(thistuple))

# creating the tuple with one item
# when creating a tuple you need to add comma after the value
# otherwise python will not recognize that this is tuple

thistuple = ("apple",)
print(thistuple)
print(type(thistuple))

# not a tuple
thistuple = ("apple")
print(thistuple)


# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# tuple can hold different data-type inside
thistuple = ("Apple", 5, "mango", False, 3, "banana")
print(thistuple)