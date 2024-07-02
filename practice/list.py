########## LIST DATA-TYPE ############

#list 1st way using square bracket
thisList = ["apple", "banana", "orange",]
print(thisList)

#list 2nd way using list() contructor
thisList_2 = list(("apple", "banana"))
print(thisList_2)

#list is orderd, changable, allow dublicate value

#dublicate value
thislist = ["apple", "banana", "cherry", "banana", "apple"]
print(thislist)

#list length check
thislist = ["apple", "banana", "cherry", "banana", "apple"]
print(len(thislist))

###list item can be any data type
list1 = ["apple", "banana", "orange"]
list2 = [1, 2, 3, 4]
list3 = [True, False, True]

print(list1)
print(list2)
print(list3)

###list can hold multiple of data type value
list4 = ["apple", "banana", 1, 2, True, 3, "cherry", 2, False]
print(list4)
print(type(list4))