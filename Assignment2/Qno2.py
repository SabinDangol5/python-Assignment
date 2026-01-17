# 2. ATM Withdrawal Simulation
# Write a Python program that:
# ● Takes the user’s account balance and withdrawal amount as input.
# ● Check if the balance is sufficient.
# ● If yes, deduct the amount and print the updated balance.
# ● If not, print “Insufficient balance”.

# Take inputs for users
balance = float(input("Enter your account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))

# Check balance and print output
if withdraw_amount <= balance:
    balance = balance - withdraw_amount
    print("Withdrawal successful.")
    print("Updated Balance after Withdraw: Rs.", balance)
else:
    print("Insufficient balance to withdraw.")
