######Temperature Calculator###########

temperature = float(input("Enter the temperature"))
scale = input("Is the Enter temperature Celcius or Farenhites? (C/F)")

if (scale.upper() == "C"):
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}C is {converted_temperature}F")
elif (scale.upper() == "F"):
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}F is {converted_temperature}")
else:
    print("Enter the correct temperature scale")
