######### Creating Personal Budget Calculator #########
monthly_income = float(input("Enter your Monthly Income: "))
rent = float(input("Enter your Monthly Rent: "))
groceries = float(input("Enter your Monthly Groceries: "))
utility_bills = float(input("Enter you Monthly Utility Bills: "))

total_expense = rent + groceries + utility_bills
net_saving = monthly_income - total_expense

saving_goal = 500
met_saving_goals = net_saving >= saving_goal

over_spent = total_expense > monthly_income

print("\n------Budget Summary------")
print(f"Your total salary is: {monthly_income:.2f}")
print(f"Your total expense is: {total_expense:.2f}")
print(f"your net saving is: {net_saving:.2f}")

if met_saving_goals:
  print(f"Congratulations! You have met your saving goal of {saving_goal:.2f}")
else:
  print(f"You have not met your saving goal of {saving_goal:.2f} keep trying")

if over_spent:
  print(f"You have over spent your monthly income of {monthly_income:.2f}")
else:
  print(f"You have not over spent your monthly income of {monthly_income:.2f}")
