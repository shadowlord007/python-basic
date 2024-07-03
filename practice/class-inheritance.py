########## Inheritance in Class in the  Python ################

# we have created a base class and derived calss which can access all
# properties and method of base class which we inharit 
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __str__(self):
        return f"my First name is {self.fname} and my last name is {self.lname}"
    
    def firstname(self):
        print(self.fname)
    def lastname(self):
        print(self.lname)
             
class Student(Person):
    pass

p1 = Student("Awais", "Akram")
p1.firstname()
p1.lastname()


# if We want to add the __init__() function to the child class 
# (instead of the pass keyword).

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    # def __str__(self):
    #     return f"my First name is {self.fname} and my last name is {self.lname}"
    
    def firstname(self):
        print(self.fname)
    def lastname(self):
        print(self.lname)
             
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

p1 = Student("Awais", "Akram")
p1.firstname()
p1.lastname()

# if We want to add the __init__() function to the child class 
# (instead of the pass keyword).
# we ca also use super() function that will let the child class to
# inherit all the method of base class

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def firstname(self):
        print(self.fname)
    def lastname(self):
        print(self.lname)
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # here we pass the value directly
        self.graduationyear = 2023
s1 = Student("Muhammad", "Awais")
s1.firstname()
s1.lastname()
print(s1.graduationyear)

# if We want to add the __init__() function to the child class 
# (instead of the pass keyword).
# we ca also use super() function that will let the child class to
# inherit all the method of base class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        return f"{self.firstname} {self.lastname}"
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # we can also give the varibale then in out init 
        # one more parameter will bwe added
        self.graduationyear = year
    
    def welcome(self):
        print(f"welcome", self.printname(), "to the class of", self.graduationyear)
        
s1 = Student("Muhammad", "Awais", 2024)
s1.welcome()