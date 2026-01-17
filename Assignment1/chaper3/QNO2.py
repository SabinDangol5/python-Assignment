# Create a simple calculator that takes two numbers and an operator (+, -, *, /) and prints
# the result.

num1=float(input("Enter first number: "))
num2=float(input("Enter seconf number: "))
operator=input("Which operator you want to perform(+,-.*,/): ")

match operator:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1*num2)

    case "/":
        print(num1 /num2)

    case _:
        print("invalid choice") 