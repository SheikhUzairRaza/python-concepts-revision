# Example: Working with Lists in Python

# Defining a list
a = [54, 23, 10, 99, -90]

# Pre-defined functions for lists
print("Length of the list:", len(a))  # Returns the number of elements in the list
print("Maximum value in the list:", max(a))  # Returns the largest element in the list
print("Minimum value in the list:", min(a))  # Returns the smallest element in the list
print("Sum of all elements in the list:", sum(a))  # Returns the sum of all elements

# Mutable vs Immutable Data Types:
# Lists are mutable (can be modified).
# Tuples are immutable (cannot be modified).

# List Methods:
# Append: Adds an element at the end of the list
print("\nOriginal list:", a)
a.append(100)
print("After appending 100:", a)
a.append(-100)
print("After appending -100:", a)

# Insert: Adds an element at a specific position
a.insert(3, 'Python')  # Inserts 'Python' at index 3
print("After inserting 'Python' at index 3:", a)

a.insert(400, 'Hello')  # If the index is out of range, it inserts at the end
print("After inserting 'Hello' at an out-of-range index:", a)

# Updating elements in a list
a[0] = 100  # Updates the first element
a[-1] = 100  # Updates the last element
print("After updating first and last elements:", a)

# Trying to update an index that doesn't exist would raise an IndexError
# Uncomment the following line to see the error:
# a[99] = 3

# Removing elements from the list:
# Pop: Removes the last element if no index is provided
a.pop()
a.pop()
print("After popping last two elements:", a)

# Pop with an index: Removes the element at the specified index
a.pop(0)  # Removes the first element
print("After popping the element at index 0:", a)

# Uncomment the following line to see IndexError when the index is out of range:
# a.pop(50)

# Remove: Removes the first occurrence of a specified value
a.remove(100)  # Removes the first occurrence of 100
print("After removing 100:", a)

# Uncomment the following line to see ValueError when the value doesn't exist:
# a.remove(500)

# Delete: Deletes an element or the entire list
del a[0]  # Deletes the element at index 0
print("After deleting the first element using \'del\':", a)

# Uncomment the following lines to delete the entire list:
# del a
# print(a)  # This will raise a NameError because the list no longer exists.

# Clear: Removes all elements from the list, but the list itself still exists
a.clear()
print("After clearing all elements using \'clear()\':", a)
