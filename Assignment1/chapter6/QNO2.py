# Ask the user to enter 5 numbers and store them in a list. Print the list in sorted order
# (without using the sort() function).

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("\nSorted order:", numbers)
