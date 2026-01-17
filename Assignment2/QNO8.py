# 8. Club Membership Set Operations
# Write a Python program that:
# ● Stores members of Club A and Club B in sets.
# ● Prints:
# ○ Members in both clubs
# ○ Members only in Club A
# ○ Members in either club
# ○ Number of members in each category



#  members
club_a = {"sabin", "akash", "ram", "david"}
club_b = {"champa", "eva", "karan", "sabin"}

# Members in both clubs
both = club_a & club_b
print("\nMembers in both clubs:", both)
print("Number of members in both clubs:", len(both))

# Members only in Club A 
only_a = club_a - club_b
print("\nMembers only in Club A:", only_a)
print("Number of members only in Club A:", len(only_a))

# Members in either club 
either = club_a | club_b
print("\nMembers in either club:", either)
print("Number of members in either club:", len(either))
