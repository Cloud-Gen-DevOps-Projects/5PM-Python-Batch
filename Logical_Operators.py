 Logical operators in Python are used to combine multiple conditions and determine the logic between them. There are three main logical operators: and, or, and not.

1. and Operator:

The and operator returns True if both operands are True, otherwise it returns False.

Example:

x = 5
y = 10

print(x > 0 and y < 20)  # True, because both conditions are True
print(x > 0 and y > 20)  # False, because the second condition is False
print(x < 0 and y < 20)  # False, because the first condition is False

Explanation:

In the first print statement, both conditions (x > 0 and y < 20) are true (True and True), so the result is True.
In the second print statement, x > 0 is true but y > 20 is false (True and False), so the result is False.
In the third print statement, x < 0 is false (False and ...), so Python does not even evaluate the second condition (y < 20), and the result is False.



2. or Operator:

The or operator returns True if at least one of the operands is True, otherwise it returns False.

Example:

x = 5
y = 10

print(x > 0 or y < 20)   # True, because both conditions are True
print(x > 0 or y > 20)   # True, because the first condition is True
print(x < 0 or y < 20)   # True, because the second condition is True
print(x < 0 or y > 20)   # False, because both conditions are False

Explanation:

In the first print statement, both conditions (x > 0 and y < 20) are true (True or True), so the result is True.
In the second print statement, x > 0 is true (True or ...), so Python does not evaluate the second condition (y > 20), and the result is True.
In the third print statement, y < 20 is true (... or True), so Python does not evaluate the first condition (x < 0), and the result is True.
In the fourth print statement, both conditions (x < 0 and y > 20) are false (False or False), so the result is False.



3. not Operator:


The not operator is used to reverse the logical state of its operand. If a condition is True, then not will make it False, and vice versa.

Example:

x = 5
y = 10

print(not x > 0)   # False, because x > 0 is True, so not (True) is False
print(not y < 20)  # False, because y < 20 is True, so not (True) is False
print(not x < 0)   # True, because x < 0 is False, so not (False) is True


Explanation:

In the first print statement, x > 0 is true, so not (True) becomes False.
In the second print statement, y < 20 is true, so not (True) becomes False.
In the third print statement, x < 0 is false, so not (False) becomes True.

