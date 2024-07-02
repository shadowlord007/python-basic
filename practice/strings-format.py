#Format String with palaceholder to put the value inside in string

# {} inside this place holder we can put varaibles, operation, function,
#and modifier to formate the value

#this is one way
# age = 25
# txt = "My name is Awais, and i am {} year old"
# print(txt.format(age))

#can add multiple place holders for multiple value
#2nd way
# age = 25
# year = 1999
# txt = "My name is Awais, and i am {} year old. i was born in {} year"
# print(txt.format(age, year))

#3rde way
# age = 25
# year = 1999
# name = "Awais"
# txt = f"My name is {name}, and i am {age} year old. i was born in {year} year"
# print(txt)

##now we can use some other example in f-string
# price = 50
# txt = f"The price is {price} dollars"
# print(txt)

##now we can use some other example in f-string
#adding decimal in price use modifier
# price = 50
# txt = f"The price is {price:.2f} dollars"
# print(txt)

##math operation
# txt = f"The price is {40 * 2} dollars"
# print(txt)
