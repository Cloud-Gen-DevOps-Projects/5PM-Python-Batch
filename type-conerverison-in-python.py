Type conversion in Python refers to the process of converting one data type into another. Python is a dynamically-typed language, meaning variables can hold values of any type, and type casting allows you to change these values as needed. Here are some examples of type conversion in Python:

==================================================

Integer to Float Conversion:

x = 5
y = float(x)
print(y) 

# Output: 5.0
Here, int value 5 is converted to a float using the float() function.

==================================================

Float to Integer Conversion:

x = 3.7
y = int(x)
print(y)  

# Output: 3
Conversion from float to int truncates the decimal part, resulting in 3.



==================================================

String to Integer Conversion:

num_str = "10"
num_int = int(num_str)
print(num_int)  

# Output: 10
The string "10" is converted to an integer using int().




==================================================
String to Float Conversion:


float_str = "3.14"
float_num = float(float_str)
print(float_num)

# Output: 3.14
Similarly, the string "3.14" is converted to a float using float().



==================================================
Integer to String Conversion:


number = 123
str_number = str(number)
print(str_number)  

# Output: "123"
Here, the integer 123 is converted to a string "123" using str().




==================================================
List to Tuple Conversion:

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  

# Output: (1, 2, 3)
A list [1, 2, 3] is converted to a tuple (1, 2, 3) using the tuple() function.




==================================================
Tuple to List Conversion:


my_tuple = (4, 5, 6)
my_list = list(my_tuple)
print(my_list)  

# Output: [4, 5, 6]
A tuple (4, 5, 6) is converted to a list [4, 5, 6] using the list() function.





==================================================
Boolean to Integer Conversion:

bool_val = True
int_val = int(bool_val)
print(int_val)  


# Output: 1
The boolean value True is converted to an integer 1 using int().



==================================================
Integer to Boolean Conversion:


num = 0
bool_val = bool(num)
print(bool_val)  

# Output: False
An integer 0 is converted to boolean False using bool().
