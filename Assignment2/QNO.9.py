# 9. Nested Collections for School Data
# Write a Python program that:
# ● Uses a dictionary to store student names mapped to a list of subjects and marks:

# students = {
# "Alice": [("Math", 85), ("English", 92)],
# "Bob": [("Math", 78), ("English", 88)]
# }

# ● Prints each student’s average marks.
# ● Prints the subject topper.
# ● Allows adding a new student with their subjects and marks.


# student data
students = {
    "Sabin": [("Math", 85), ("English", 92)],
    "Roman": [("Math", 78), ("English", 88)]
}

#  Print each student's average marks
print("Student Averages:")
for student, marks_list in students.items():
    total = sum(mark for subject, mark in marks_list)
    avg = total / len(marks_list)
    print(f"{student}: {avg:.2f}")

# Find subject toppers
# Create a dictionary for each subject
subject_topper = {}

for student, marks_list in students.items():
    for subject, mark in marks_list:
        if subject not in subject_topper or mark > subject_topper[subject][1]:
            subject_topper[subject] = (student, mark)

print("\nSubject Toppers:")
for subject, (student, mark) in subject_topper.items():
    print(f"{subject}: {student} ({mark})")

#  Add a new student
new_name = input("\nEnter new student name: ")
n_subjects = int(input("Enter number of subjects: "))
new_marks = []
for _ in range(n_subjects):
    subject = input("Enter subject name: ")
    mark = int(input("Enter marks: "))
    new_marks.append((subject, mark))

students[new_name] = new_marks
print(f"{new_name} added successfully!")

# print updated averages
print("\nUpdated Student Averages:")
for student, marks_list in students.items():
    total = sum(mark for subject, mark in marks_list)
    avg = total / len(marks_list)
    print(f"{student}: {avg:.2f}")
