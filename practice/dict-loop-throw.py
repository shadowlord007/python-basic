########## Loop throw Dictonary in Python ################

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


# You can loop through a dictionary by using a for loop.
# Print all key names in the dictionary, one by one:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

for key in thisdict:
    print(key)
    
# we can use the keys() method to return the keys of a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

for key in thisdict.keys():
    print(key)
    
    
# Print all values in the dictionary, one by one:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

for key in thisdict:
    print(thisdict[key])

# we can also use the values() method to 
# return values of a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
for value in thisdict.values():
    print(value)

# Loop through both keys and values, by using the items() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
for key, value in thisdict.items():
    print(key, value)