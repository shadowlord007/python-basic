############ Loop throw the List item ###########

# we can loop throw the list since it it iterable
# loop throw the list with for loop

thislist = ["apple", "banana", "orange"]
print(thislist)

for item in thislist:
    print(item)
    

# we can also loop throw the list from it's range() and len()

thislist = ["apple", "ornage", "cherry"]
for item in range(len(thislist)):
    print(thislist[item])


## alos ue can use  while loop
thislist = ["apple", "banana", "orange"]
print(thislist)

item = 0

while item < len(thislist):
    print(thislist[item])
    item = item + 1

 
# Looping Using List Comprehension
# this list comprehensinve is a shorter syntex of for loop
# we willo be learn more of this in next chapter

thislist = ["apple", "banana", "orange"]
[print(item) for item in thislist]
# the result is unexpected we will learn deeply in next chapter