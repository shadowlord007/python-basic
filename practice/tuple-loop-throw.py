########## Lopping Tuple in Python ################

# For loop

thistuple = ("apple", "banana", "orange", "mango", "cherry")
print(thistuple)
# lopp throw the tuple
for item in thistuple:
    print(item)
    
# looping index of tuple
# we can also loop throw wirth range() and len() 
thistuple = ("apple", "banana", "orange", "mango", "cherry")
print(thistuple)

# lopping throw index
for item in range(len(thistuple)):
    print(thistuple[item])
    

# While loop

# we can also use while loop to loop throw tuple
thistuple = ("apple", "banana", "orange", "mango", "cherry")
print(thistuple)

item = 0
while item < len(thistuple):
    print(thistuple[item])
    item = item + 1
