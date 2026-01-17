# Ask the user to enter their monthly expenses under 5 categories (food, rent, travel,
# shopping, other). Store them in variables and print the total and average expense.


# Taking user input for each expense category
food = float(input("Enter your monthly food expense: "))
rent = float(input("Enter your monthly rent expense: "))
travel = float(input("Enter your monthly travel expense: "))
shopping = float(input("Enter your monthly shopping expense: "))
other = float(input("Enter your other monthly expenses: "))

# Calculating total and average
total = food + rent + travel + shopping + other
average = total / 5

# Displaying results
print(f"Your Total Expense: {total}")
print(f"Your Average Expense: {average}")
