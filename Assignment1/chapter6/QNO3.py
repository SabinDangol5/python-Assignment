# 3. Create a program that:
# ○ Takes 7 numbers as input into a list
# ○ Creates a new list of only even numbers
# ○ Creates another list of numbers greater than the average
# ○ Prints all three lists clearly.


# Take 7 numbers from user
numbers = []
for i in range(7):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_numbers = []
for i in numbers:
    if i%2==0:
        even_numbers.append(i)

average = sum(numbers) / len(numbers)

greater_than_average = []
for i in numbers:
    if i > average:
        greater_than_average.append(i)

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Numbers Greater Than Average:", greater_than_average)


