In Python, continue and pass are two flow control statements used within loops (like for or while) and conditional statements (if, elif, else). They serve different purposes and are used in different contexts. Let's delve into each one with examples:

1. continue statement:

The continue statement is used to skip the rest of the code inside a loop for the current iteration, and to proceed to the next iteration. It can be particularly useful when you want to skip certain elements or conditions within a loop.

Syntax:


for item in sequence:
    if condition:
        continue

    # other code inside the loop


Example:


# Print only odd numbers from 1 to 10

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

Explanation:

In this example, the loop iterates from 1 to 10 (range(1, 11)).

The if i % 2 == 0: condition checks if i is even.

If i is even, continue is executed, skipping the print(i) statement and moving to the next iteration.

If i is odd, print(i) is executed, thus printing the odd numbers.




2. pass statement:

The pass statement is a null operation; it means it does nothing when it executes. It acts as a placeholder where syntax requires a statement but you have nothing to do. It is often used during development when you want to implement an empty code block without causing errors.


Syntax:


if condition:
    pass  # do nothing
else:
    # do something else



Example:

# Function that doesn't do anything yet
def placeholder_function():
    pass


Explanation:

pass is used here as a placeholder inside the function placeholder_function().

If you define a function but haven't implemented its logic yet, you can use pass to avoid syntax errors until you are ready to write the function's code.

It's also used in conditional statements where you need to have a code block for both the if and else branches, but you don't want to execute any code for a specific condition.

Usage scenarios:

Loops: When you need to structure your loop but want to skip certain iterations based on conditions.
Functions and classes: When defining placeholders for future implementation.
Conditionals: When you need a placeholder in both branches of an if-else statement



==================================================

Example 1: Using continue to skip even numbers


# Print only odd numbers from 1 to 10 using continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
Output:

1
3
5
7
9

Explanation:

In this program, we use a for loop to iterate over numbers from 1 to 10 (range(1, 11)).
The if i % 2 == 0: condition checks if the current number i is even.
If i is even (i % 2 == 0), the continue statement is executed, which skips the rest of the loop's body for that iteration.
If i is odd, the print(i) statement is executed, printing the odd numbers.

====================================================
Example 2: Using pass as a placeholder


# Define a function that is not yet implemented
def placeholder_function():
    pass

# Call the function
placeholder_function()

# No output is produced because the function does nothing


Explanation:

In this example, placeholder_function() is defined but not yet implemented.
The pass statement inside placeholder_function() acts as a placeholder, indicating that the function doesn't perform any actions yet.
When placeholder_function() is called, it does nothing and produces no output.

=======================================================
Example 3: Using pass in conditional statements



# Example of using pass in an if-else statement
def check_condition(value):
    if value > 0:
        print("Value is positive")
    elif value < 0:
        print("Value is negative")
    else:
        pass  # Placeholder for handling zero (no action currently)

# Test the function
check_condition(5)
check_condition(-3)
check_condition(0)


Output:

Value is positive
Value is negative

Explanation:

In this example, the check_condition() function checks whether the input value is positive, negative, or zero.
Inside the else: block, pass is used as a placeholder. Currently, there's no specific action defined for the case where value is zero.
When value is 0, the pass statement is executed, which means no action is taken in that branch of the conditional statement.



=======================================================

Using Python continue in a while loop example

The following example shows how to use the continue statement to display odd numbers between 0 and 9 to the screen:

# print the odd numbers 
counter = 0
while counter < 10:
    counter += 1

    if not counter % 2:
        continue

    print(counter)
Code language: Python (python)


Output:

1
3
5
7
9

Code language: Python (python)

How it works.

First, define the counter variable with an initial value of zero
Second, start the loop as long as the counter is less than 10.
Third, inside the loop, increase the counter by one in each iteration. If the counter is an even number, skip the current iteration. Otherwise, display the counter to the screen.

