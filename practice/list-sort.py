############ List Sort ###########

# we can sort the list alphanumerically
# sort() method
# this method will sort the list alphanumarically and assecdeing order by default
thislist = ["apple", "orange", "banana", "mango", "kiwi"]
print(thislist)
thislist.sort()
print(thislist)

# sorting numeric value assecding order

thislist = [100, 20, 50, 19, 37, 60]
print(thislist)
thislist.sort()
print(thislist)


# sort method can also do the desecding order by give value
# in parantheses like revers = true
thislist = ["apple", "orange", "banana", "mango", "kiwi"]
print(thislist)
thislist.sort(reverse = True)
print(thislist)

# also with numeric value
thislist = [100, 20, 50, 19, 37, 60]
print(thislist)
thislist.sort(reverse = True)
print(thislist)


# we can also create our own order for the list to sort
# how ever we want be making a function key = function
# example the value that is close to 50 willbe sort first
def myfunc(n):
    return abs(n - 50)
thislist = [100, 20, 50, 19, 37, 60]
print(thislist)
thislist.sort(key=myfunc)
print(thislist)

## if want to sort the current list to reverse without the aphanumeric
# based then we use reverse() method
thislist = ["apple", "orange", "banana", "mango", "kiwi"]
print(thislist)
thislist.reverse()
print(thislist)

