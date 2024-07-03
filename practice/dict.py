########## Dictonary in Python ################

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, 
# changeable and do not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# we can also use dict() constructor to create dict

thisdict = dict(brand= "Ford", model = "Mustang", year = 1964)
print(thisdict)

# we can get the single value as
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["model"])


# Dictionaries are changeable, meaning that we can change, 
# add or remove items after the dictionary has been created.

# Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "model": "Honda",
    "year": 1964,
    "year": 2020
}
print(thisdict)


# len() to check the length of dict
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))


# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
# this values have list so this is how we access it
print(thisdict["colors"][2])
print(type(thisdict))