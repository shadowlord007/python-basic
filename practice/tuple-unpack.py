########## Unpack Tuple in Python ################

# when we create a tuple we are simply packing a tuple
thistuple = ("apple", "banana")
print(thistuple)

#But, in Python, we are also allowed to extract the values back 
# into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
print(fruits)

#here we have to use round bracket to extract the value from tuple
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# if the number of variable is not match to the number of value in tuple
# we can use asteric (*) to get the remaing value from tuple as a list
fruits = ("apple", "banana", "cherry", "respberry")
print(fruits)

# here we have to use round bracket to extract the value from tuple
# and the red will take a list of value
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values 
# left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# here the tropic will get list unltil the last value remain for the
# last variable
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)