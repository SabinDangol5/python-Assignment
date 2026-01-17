# Take a string input from the user and display:
# ○ The length of the string
# ○ The first and last characters
# ○ The reversed string


text = input("Enter a string: ")

print("Length of the string: ", len(text))
print("First character: ", text[0])
print("Last character: ", text[-1])
print("Reversed string: ", text[::-1])
