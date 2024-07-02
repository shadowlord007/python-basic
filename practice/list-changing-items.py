############ Changing list item ###########

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)

# can also change the range of list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[2:5] = ["strawberry", "lemon", "blackcurrant"]
print(thislist)

# can also insert more item then the range specified
# the the new value will be inserted where you speccified the range and existed item will move after the inserted one
thislist = ["apple", "banana", "cherry", "blackcurrant"]
thislist[1:2] = ["strawberry", "mango"]
print(thislist)

# it also have other effect to if the you enter less value the the range specified
#then it will reoplace all of the range with in the inserted value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["strawberry"]
print(thislist)


#insert() this is method that take 2 parameter 1 is where to and 2nd is what to insert
##Insert item in to the list
#this will inser the item into the list woithout removing or replacing existed item in list

thislist = ["apple"]
thislist.insert(1, "banana")
print(thislist)
thislist.insert(1, "cherry")
print(thislist)
thislist.insert(0, "mango")
print(thislist)
