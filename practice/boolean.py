########Boolean Vlaues#########
# print(10 > 9)  #True
# print(10 == 9)  #False
# print(10 < 9)  #False

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("Hello"))
# print(bool(15))

# lmost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

###here calss return 0 which mean the bool is False
# class myclass():

#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))

###function return value can also be True or False
# def myFunction():
#   return True

# print(myFunction())

####Base ion the reurn value from function we can check the if condition
# def myFunction():
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

### many built-in function also return True or False
#this check if the vlaue is integer or not
# x = 200
# print(isinstance(x, int))
