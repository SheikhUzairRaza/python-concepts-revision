# Define a list
a = [55, 43, 12, "uzair", "sur", -88, 99]

# Iterate by index/position
print("\nIterate by index/position:")
for i in range(len(a)):
    print(a[i], end=" ")
print()

# Iterate by value
print("\nIterate by value:")
for value in a:
    print(value, end=" ")
print()

# Reverse iteration
print("\nIterate in reverse order:")
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
print()

# Print even numbers in a custom list
my_list = [51, 74, 85, 91, 52, 44]
print("\nEven numbers in the list are:")
for num in my_list:
    if num % 2 == 0:
        print(num, end=" ")
print()

# Print odd numbers in a custom list
print("\nOdd numbers in the list are:")
for num in my_list:
    if num % 2 != 0:
        print(num, end=" ")
print()

# Print elements at even indexes
print("\nElements present at even indexes:")
for i in range(len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")
print()

# Sum of all elements in the list
total = sum(my_list)  # Using built-in sum function
print(f"\nTotal sum of elements in {my_list} is {total}")

# Alternative way to calculate the sum using a loop
total2 = 0
for num in my_list:
    total2 += num
print(f"Total2 sum of elements in {my_list} is {total2}")

# Count the number of even numbers in the list
even_count = sum(1 for num in my_list if num % 2 == 0)
print(f"\nNumber of even numbers in the list: {even_count}")

# Count numbers divisible by both 2 and 5
count2_5 = sum(1 for num in my_list if num % 2 == 0 and num % 5 == 0)
print(f"Numbers divisible by 2 and 5: {count2_5}")

# Find the largest number in the list
largest = max(my_list)  # Using the built-in max function
print(f"The largest number in the list is: {largest}")

# Alternative way to find the largest number using a loop
largest_alternative = my_list[0]
for num in my_list:
    if num > largest_alternative:
        largest_alternative = num
print(f"The largest number using a loop is: {largest_alternative}")
