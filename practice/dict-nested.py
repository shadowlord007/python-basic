########## Nested Dictonary in Python ################

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# we can also create three seperate dictionary and then add them into one.
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
print(child1)
print(child2)
print(child3)

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}
print(myfamily)

# To access items from a nested dictionary, you use the name of the 
# dictionaries, starting with the outer dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
print(child1)
print(child2)
print(child3)

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}
print(myfamily["child2"]["name"])


# we can loop through a dictionary by using the 
# items() method like this:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

for key, value in myfamily.items():
    print(key)
    for item in value:
        print(item + ':', value[item])