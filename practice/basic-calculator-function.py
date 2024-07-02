#######Basic Calculator########
#Create a program that performs basic arithmetic operations.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))


def sum(number1, number2):
  sum = number1 + number2
  return sum


sumOfNumber = sum(number1, number2)
print("The sum of two number is {}".format(sumOfNumber))


def diffrence(number1, number2):
  diffrence = number1 - number2
  return diffrence


diffrenceOfNumber = diffrence(number1, number2)
print("The difference of two number is {}".format(diffrenceOfNumber))


def product(number1, number2):
  product = number1 * number2
  return product


productOfNumber = product(number1, number2)
print("The product of two number is {}".format(productOfNumber))


def devide(number1, number2):
  devide = number1 / number2
  return devide


devideOfNumber = devide(number1, number2)
print("The devide of two number is {}".format(devideOfNumber))
