# Simulating a do-while loop to ask the user for input until a valid number is entered

while True:
    user_input = input("Enter a number greater than 10: ")
    number = int(user_input)
    if number > 10:
        break  # Exit the loop if a valid number is entered

print("Valid number entered:", number)





# Another way to simulate a do-while loop using a flag variable

valid = False

while not valid:
    user_input = input("Enter your username: ")
    if len(user_input) >= 5:
        valid = True  # Set valid to True if the condition is met

print("Username accepted:", user_input)





# Simulating a menu-driven program using a do-while loop

while True:
    print("\nMenu:")
    print("1. Calculate area of a rectangle")
    print("2. Calculate area of a circle")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        area = length * width
        print(f"Area of rectangle: {area}")
    elif choice == '2':
        radius = float(input("Enter radius of circle: "))
        area = 3.14 * radius * radius
        print(f"Area of circle: {area}")
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")





# Simulating password validation using a do-while loop

correct_password = "P@ssw0rd"
while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Please try again.")




# Simulating data input validation using a do-while loop

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue  # Go to the beginning of the loop to ask for input again
        else:
            break  # Exit the loop if a valid age is entered
    except ValueError:
        print("Invalid input. Please enter a valid integer age.")

print(f"Your age is: {age}")




# Simulating a do-while loop to validate user input

while True:
    try:
        num = int(input("Enter a positive number: "))
        if num <= 0:
            print("Number must be positive. Please try again.")
            continue  # Continue the loop to ask for input again
        else:
            break  # Exit the loop if a positive number is entered
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"You entered: {num}")





# Processing elements in a list using a do-while style loop (using Python's built-in iterator)

data = [10, 20, 30, 40, 50]
it = iter(data)

while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break




# Simulating a game loop using a do-while style approach

import random

while True:
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)
    guess = None

    while guess != target_number:
        guess = int(input("Guess the number (between 1 and 10): "))
        if guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

print("Game over. Thanks for playing!")




# Simulating printing multiplication tables using a do-while style loop

while True:
    try:
        num = int(input("Enter a number to print its multiplication table (enter 0 to exit): "))
        
        if num == 0:
            print("Exiting program...")
            break  # Exit the loop if user enters 0
        
        print(f"Multiplication Table for {num}:")
        i = 1
        
        while True:
            print(f"{num} x {i} = {num * i}")
            i += 1
            if i > 10:
                break  # Exit inner loop after printing 10 times
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

