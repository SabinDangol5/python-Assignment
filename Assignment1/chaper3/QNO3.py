# Write a program that calculates the final price of an item after applying both a discount and tax. 
# The user enters:
# ○ Original price
# ○ Discount percentage 
# ○ Tax percentage 
# Print the final amount after applying discount first, then tax.


# Take inputs from the user
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter discount percentage: "))
tax_percent = float(input("Enter tax percentage: "))

# Calculate price after discount
discount_amount = (discount_percent / 100) * original_price
price_after_discount = original_price - discount_amount

# Calculate tax on discounted price
tax_amount = (tax_percent / 100) * price_after_discount

# Final price
final_price = price_after_discount + tax_amount

# Print result
print("\n----- Final Price Calculation -----")
print(f"Price after discount: {price_after_discount}")
print(f"Tax added: {tax_amount}")
print(f"Final price: {final_price}")
