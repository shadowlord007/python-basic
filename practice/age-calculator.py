############ Age Calculator #################
birthYear = int(input("Enter your birth Year"))

current_year = int(input("Enter the current Year"))

vote_eligibilty = 18
if (birthYear <= 0):
    print("enter the correct Birth Year")
else: 
    age = current_year - birthYear
    print(f"Your age is {age} year")

    if (age < vote_eligibilty):
        print(f"Your are less then {vote_eligibilty} year old, SO wait {vote_eligibilty - age} more year for vote")
    else:
        print(f"congratulation yor are Eligiblle for the vote")