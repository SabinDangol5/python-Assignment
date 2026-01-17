# 7. Word Frequency Counter
# Write a Python program that:
# ● Takes a paragraph of text from the user.
# ● Count how many times each word appears ( remember the case sensitivity and
# punctuation).
# ● Prints the frequency of each word.


# Take paragraph input for user
text = input("Enter a paragraph: ")

# Split the text into words 
words = text.split()

# Create an empty dictionary to store frequencies
freq = {}

# Count each word
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Print frequencies of each word
print("\nWord Frequencies:")
for word, count in freq.items():
    print(word, ":", count)
