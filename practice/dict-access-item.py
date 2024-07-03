########## Accessing item of Dictonary in Python ################

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


# we can access the value in dict like this 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
model = thisdict["model"]
print(model)

# also can use get() method same as thisdict["model"] this
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
model = thisdict.get("model")
print(model)


# the keys() method will retuen all the keys in dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys())


# Add a new item to the original dictionary, 
# and see that the keys list gets updated as well:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

key = car.keys()
print(key)

car["color"] = "red"

print(key)


# the vlaues() method will return all the values in the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.values())

#Make a change in the original dictionary, and see that the values 
# list gets updated as well:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

value = car.values()
print(value)

car["year"] = "2024"

print(value)

# Add a new item to the original dictionary, and see that the 
# values list gets updated as well:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

value = car.values()
print(value)

car["color"] = "blue"

print(value)



# The items() method will return each item in a dictionary, 
# as tuples in a list.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.items())

# Make a change in the original dictionary, and see that the items 
# list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# Add a new item to the original dictionary, and see that the items 
# list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


# To determine if a specified key is present in a 
# dictionary use the in keyword:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)

if "model" in car:
     print("Yes, 'model' is one of the keys in the car dictionary")

