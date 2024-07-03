########## Access Sets in Python ################

thisset = {"apple", "banana", "cherry", "mango"}
print(thisset)

# we cannot access the set values by index or key
# but we can use for loop to loop throw the sets
# and also we can check if the specific value present in set

thisset = {"apple", "banana", "cherry", "mango"}
print(thisset)

for item in thisset:
    print(item)
    
# chjech if the value is present in set
thisset = {"apple", "banana", "cherry", "mango"}
print("apple" in thisset)

# chjech if the value is not present in set
thisset = {"apple", "banana", "cherry", "mango"}
print("melon" not in thisset)