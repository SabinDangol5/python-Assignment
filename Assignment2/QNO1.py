# 1. Supermarket Billing System
# Write a Python program that:
# ● Takes the total bill amount as input from the user.
# ● Applies a discount:
# ○ Less than 500 → 0%
# ○ 500–1000 → 5%
# ○ More than 1000 → 10%
# ● Prints the final amount after discount.


# Take total bill amount as input from user
bill_amount = float(input("Enter total bill amount: "))

# Apply discount
if bill_amount < 500:
    discount = 0
elif bill_amount <= 1000:
    discount = bill_amount * 0.05
else:
    discount = bill_amount * 0.10

# Calculate final amount
final_amount = bill_amount - discount

# Print result
print("Discount Applied: Rs.", discount)
print("Final Amount after Discount: Rs.", final_amount)
