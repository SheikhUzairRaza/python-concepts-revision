# Example Problem: Storing multiple marks for students
# If we store marks as individual variables, values can be overridden.

# Marks of the first student (overwritten below):
english = 32
maths = 45
science = 78
urdu = 78
history = 78

# Marks of the second student (overwrites the first student's data):
english = 33
maths = 45
science = 79
urdu = 78
history = 78

# To avoid overriding and efficiently store multiple values, we use Lists in Python.

"""
Lists:
Lists allow us to store multiple values in a single variable.
"""

# Marks of two students using lists
first_student = [32, 45, 78, 78, 78]  # Marks of the first student
second_student = [33, 45, 79, 78, 78]  # Marks of the second student

# Printing the lists
print(first_student)
print(second_student)

# Checking the type of the variables to confirm they are lists
print(type(first_student), type(second_student), sep=" ")