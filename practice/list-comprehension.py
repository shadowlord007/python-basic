############ List Comprehension ###########

# what is the role of list Comprehension
# if we want to create a new list based on the existed list
# only with specifed value like i want to create a new list 
# from existed list and and check if the list have this value
# only these items will; be addeed ti the new list

# eithe we do it with for lop and apply the conditon and then save
#into new list example

fruits = ["apple", "banana", "orange", "kiwi", "cherry", "mango"]
new_fruits = []

for fruit in fruits:
    if "a" in fruit:
        new_fruits.append(fruit)

print(new_fruits)


# But with the list Comprehension we can do this in single line
# and check all the above code into more shorter way example

fruits = ["apple", "banana", "orange", "kiwi", "cherry", "melon", "mango", "strawberry", "pineapple"]
print(fruits)
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)


# now let flter the comprehension with proper item
fruits = ["apple", "banana", "orange", "kiwi", "cherry", "melon", "mango", "strawberry", "pineapple"]
print(fruits)
new_fruits = [fruit for fruit in fruits if fruit != "apple"]
print(new_fruits)

# what happend with the comprehension if we did not use if condion then
# it gonna return all the list to new list without changing the orginal list
fruits = ["apple", "banana", "orange", "kiwi", "cherry", "melon", "mango", "strawberry", "pineapple"]
print(fruits)
new_fruits = [fruit for fruit in fruits]
print(new_fruits)

## the iterable can be any objet, list, tuple, set etc
newlist = [item for item in range(10)]
print(newlist)

## the iterable can be any objet, list, tuple, set etc now with if condtion
newlist = [item for item in range(10) if item < 5]
print(newlist)


# the expression we use in comprehension list we can also munipiulate it before
# it store valaue in list
## the iterable can be any objet, list, tuple, set etc
fruits = ["apple", "banana", "orange", "kiwi", "cherry", "melon", "mango", "strawberry", "pineapple"]
print(fruits)
new_fruits = [fruit.upper() for fruit in fruits]
print(new_fruits)

## we can also munipulte the outcome to what ever we want lke every time
# comprehension list loop run we change the value to whatever we want
# now this will print the outcome 10 times
newlist = ['Assalam-o-alikum' for item in range(10)]
print(newlist)


#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
fruits = ["apple", "banana", "orange", "kiwi", "cherry", "melon"]
print(fruits)
new_fruits = [fruit if fruit != "banana" else "mango" for fruit in fruits]
print(new_fruits)
