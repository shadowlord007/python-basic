########## Access Python List ############

thislist = ["apple", "banana", "orange"]
print(thislist[0])

#also use negative index
thislist = ["apple", "banana", "orange"]
print(thislist[-1])

#Range of index to acces the list with negative index
#sama as postive index range
#postive range start from start of list
#negative range start from the end of list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-5:-1])

#Check if the specific item exist in list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
    print("Yes, apple in the fruit list")