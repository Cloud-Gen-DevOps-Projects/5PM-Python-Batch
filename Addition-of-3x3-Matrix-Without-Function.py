# Initialize the first matrix
print("Enter elements for the first 3x3 matrix:")
matrix1 = []
for i in range(3):
    row = []
    for j in range(3):
        element = float(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)

# Initialize the second matrix
print("\nEnter elements for the second 3x3 matrix:")
matrix2 = []
for i in range(3):
    row = []
    for j in range(3):
        element = float(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix2.append(row)

# Add the matrices
result_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        sum_element = matrix1[i][j] + matrix2[i][j]
        row.append(sum_element)
    result_matrix.append(row)

# Print the resulting matrix after addition
print("\nThe resulting matrix after addition is:")
for row in result_matrix:
    print(row)
