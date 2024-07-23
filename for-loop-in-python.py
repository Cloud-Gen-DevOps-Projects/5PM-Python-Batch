In Python, a for loop is used to iterate over a sequence (such as a list, tuple, string, or any iterable object) and execute a block of code for each element in the sequence. The for loop syntax in Python is straightforward:


for item in sequence:

    # do something with item
Here's how it works:

item: This is a variable that takes each item from the sequence one by one.
sequence: This is the iterable object (like a list, tuple, string, etc.) over which the loop iterates.


Examples:
Iterating over a list:


# Iterating over a list of numbers

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)



Output:

1
2
3
4
5

Iterating over a string:


# Iterating over characters in a string

greeting = "Hello"
for char in greeting:
    print(char)


Output:

H
e
l
l
o
Iterating over a range of numbers:


# Iterating using range function
for i in range(1, 6):
    print(i)


Output:

1
2
3
4
5

Notes:

The for loop in Python is versatile and can iterate over any iterable object.
You can use the range() function to generate a sequence of numbers to iterate over.
The loop continues until all items in the sequence have been processed.
Inside the loop block (indented part), you can perform operations on each item or use the item in calculations or conditions.
