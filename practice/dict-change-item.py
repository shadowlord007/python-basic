########## Change item of Dictonary in Python ################

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

# chnage item in dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)