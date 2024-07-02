# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different
#types can do different things

# Python has the following data types built-in by default, in #these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# lets dive into numeric Data Types
# Python Numbers
# There are three numeric types in Python:

# int it can be unlimited postive and negative values

# float it can be unlimited value containt one or more deciaml
#postive and negative values it can alos use e for the power
#of 10

# complex this is imaginary values postive or negative

# x = 1
# y = 2.8
# z = 1j

# a = -5j
# b = 2 + 5j

# c = 12e4  #power of 10
# print(x)
# print(y)
# print(z)

# print(a)
# print(b)

# print(c)

# print(type(x))  #int
# print(type(y))  #float
# print(type(z))  #complex

# print(type(a))  #imaginary
# print(type(b))  #imaginary

# print(type(c))  #float

#we can convert int into float, float into int, int into complex, float into complex.
#but we can not convert complex into int, float.
# x = 10
# y = 10.5
# z = 1j

# print(float(x))
# print(complex(x))

# print(int(y))
# print(complex(y))

#python does not have a random() function to make a random number, by importing random.
#but python has a built-in module called random that can
#generate the random number between range

#import random

#print(random.randrange(1, 10))  #generate number excluding 10
#print(random.randint(1, 20))  #genrate number including 20
