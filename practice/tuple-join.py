########## Join Tuples in Python ################


tuple1 = ("apple", "banana", "orange", "mango", "cherry")
print(tuple1)
tuple2 = ("strawberry", "kiwi", "pineapple")
print(tuple2)
tuple3 = (1, 2, 3, 4, 5)
print(tuple3)

thistuple = tuple1 + tuple2 + tuple3
print(thistuple)

#If you want to multiply the content of a tuple a given 
# number of times, you can use the (*) operator:
tuple1 = ("apple", "banana", "orange", "mango", "cherry")

thistuple = tuple1 * 2
print(thistuple)