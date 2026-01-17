# 3. Pyramid Star Pattern
# Write a Python program that:
# ● Takes a number n as input.
# ● Prints a pyramid of stars with n rows.
# ● Example for n = 5:
# *
# ***
# *****
# *******
# *********


# take no of rows as input for users

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    stars = 2 * i - 1      # calculate number of stars  
    print("*" * stars)           
