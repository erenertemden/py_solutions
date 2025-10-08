# List: ordered, mutable, allows duplicates

my_list = [1, 2, 3, 4, 5, "banane", True]

print(my_list)

print(type(my_list))

print(len(my_list))

print(my_list[0])  # First element

print(my_list[-1])  # Last element

print(my_list[1:4])  # Slicing

my_list[0] = 10  # Modify element

print(my_list)

my_list.append("new item")  # Add element

my_list.insert(1, "inserted item")  # Insert element at index 1

print(my_list)

my_list.remove(3)  # Remove element

print(my_list)

my_list.pop()  # Remove last element

print(my_list)

my_list.sort()  # Sort list (only works if all elements are of the same type

print(my_list)

my_list.reverse()  # Reverse list

print(my_list)

print(my_list.count(2))  # Count occurrences of an element

my_list.clear()  # Clear list

print(my_list)

print(len(my_list))  # Length of list

my_list = [1, 2, 3, 4, 5, "banane", True]

for item in my_list:  # Iterate through list

    print(item)

print(3 in my_list)  # Check if element exists

new_list = my_list + [6, 7, 8]  # Concatenate

print(new_list)

print(new_list * 2)  # Repeat

print(min([1, 2, 3, 4, 5]))  # Minimum value

print(max([1, 2, 3, 4, 5]))  # Maximum value

print(sum([1, 2, 3, 4, 5]))  # Sum of elements

print(sorted([3, 1, 4, 2, 5]))  # Sorted list

print(list("hello"))  # Convert string to list

print(list((1, 2, 3)))  # Convert tuple to list

print(list({1: "a", 2: "b"}))  # Convert dictionary

print(list(range(5)))  # Convert range to list

print(list(set([1, 2, 2, 3, 4, 4, 5])))  # Convert set to list

print([x**2 for x in range(10)])  # List comprehension

print([x for x in my_list if isinstance(x, int)])  # Filter integers

print([x for x in my_list if isinstance(x, str)])  # Filter strings

print([x for x in my_list if isinstance(x, bool)])  # Filter boole

print([x for x in my_list if isinstance(x, (int, float))])  # Filter numbers

print([x for x in my_list if isinstance(x, (str, bool))])  # Filter strings and booleans

print([x for x in my_list if isinstance(x, (int, str))])  # Filter integers and strings

print([x for x in my_list if isinstance(x, (float, bool))])  # Filter floats and booleans

print([x for x in my_list if isinstance(x, (int, float, str))])  # Filter numbers and strings