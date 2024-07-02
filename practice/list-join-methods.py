############ List Joins ###########

#There are several ways to join, or concatenate, 
# two or more lists in Python.
# we can use + operator to join the list

# 1st way
fruits = ["apple", "orange", "banana", "mango", "kiwi"]
number = [100, 20, 50, 19, 37, 60]

list3 = fruits + number
print(fruits)
print(number)

print(list3)


# Another way to join two lists is by appending all the items from list2 into list1, one by one:

fruits = ["apple", "orange", "banana", "mango", "kiwi"]
numbers = [100, 20, 50, 19, 37, 60]
print(fruits)
print(number)

for number in numbers:
    fruits.append(number)

print(fruits)


# we can use the extend() method, where the purpose is to add 
# elements from one list to another list:
fruits = ["apple", "orange", "banana", "mango", "kiwi"]
numbers = [100, 20, 50, 19, 37, 60]
print(fruits)
print(number)

fruits.extend(numbers)
print(fruits)



############### List Method ###############

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
