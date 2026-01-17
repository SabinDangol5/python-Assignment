# 5. Grocery Inventory System (Tuple & List)
# Write a Python program that:
# ● Stores product names in a tuple and stock quantities in a list.
# ● Allows the user to:
# ○ Check product availability
# ○ Update stock after purchase
# ○ Display all products with their available quantities



products = ("rice", "sugar", "oil", "salt")
stock = [50, 30, 20, 40]

while True:
    print("\n1. Check product availability")
    print("2. Buy product (update stock)")
    print("3. Display all products")
    print("4. Exit")

    choice = int(input("Enter your choice(1-4): "))

    match choice:

        case 1:
            name = input("Enter product name: ")
            if name in products:
                i = products.index(name)
                print("Available quantity:", stock[i])
            else:
                print("Product not found")

        case 2:
            name = input("Enter product name: ")
            if name in products:
                i = products.index(name)
                qty = int(input("Enter quantity to buy: "))
                if qty <= stock[i]:
                    stock[i] = stock[i] - qty
                    print("Purchase successful")
                else:
                    print("Not enough stock")
            else:
                print("Product not found")

        case 3:
            print("\nProduct List:")
            for i in range(len(products)):
                print(products[i], ":", stock[i])

        case 4:
            print("Thank you!")
            break

        case _:
            print("Invalid choice")

