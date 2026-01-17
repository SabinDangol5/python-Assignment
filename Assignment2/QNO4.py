# 4. Factorial, Fibonacci, and Prime Check
# Write a Python program that:
# ● Takes a number as input.
# ● Prints its factorial.
# ● Prints the Fibonacci series up to that number.
# ● Checks and prints whether the number is prime or not.


# For Factorial, Fibonacci, and Prime Check

n = int(input("Enter a number: "))

#  Factorial 
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print("Factorial of Given Num:", fact)

#   Fibonacci Series 
a = 0
b = 1
print("Fibonacci series:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()

# Prime Check 
if n <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Given num is Prime number")
    else:
        print("Given num is Not a prime number")
