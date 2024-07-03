########### Classes and Object in Python ###############
# Create class
# class is keyword which create class with specific name

class MyClass:
    x = 5
    
p1 = MyClass()
print(p1.x)

# lets create a person class
# the calss have built-in function __init__()
# this functiuon is called every time the we asign a object to the class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Awais", 25)
print(p1.name)
print(p1.age)


# another function in class is
# __str__()
# this function will controll what will be return when class
# object is called

# without using the __str__() example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Awais", 25)
print(p1)

# using the __str__() example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
    
p1 = Person("Awais", 25)
print(p1)


# Objects can also contain methods. 
# Methods in objects are functions that belong to the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Assalam-O-Alikum my name is " + self.name)
p1 = Person("Awais", 25)
p1.myfunc()

#The self parameter is a reference to the current instance of 
# the class, and is used to access variables that belongs to 
# the class.

#It does not have to be named self , you can call it whatever 
# you like, but it has to be the first parameter of any 
# function in the class:

#example

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
        
    def myfunc(mysillyobject):
        print(f"My name is {mysillyobject.name}")
p1 = Person("Awais Akram", 25)
p1.myfunc()


# we can manipulate the object and change it's properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Awais-Akram", 25)

p1.age = 30

print(p1.name)
print(p1.age)


### Delete Object
# we ca also delete the object of the class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Awais-Akram", 25)

p1.age = 40
# del p1
print(p1.name)
print(p1.age)

# class object cannot be empty
# for empty class we will use pass keyword to not get error
class Person:
    pass