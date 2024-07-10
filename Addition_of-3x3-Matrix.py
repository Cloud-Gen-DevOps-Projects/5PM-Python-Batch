def create_matrix():
    matrix = []
    print("Enter the elements of the 3x3 matrix row-wise:")
    for i in range(3):
        row = []
        for j in range(3):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            sum_element = matrix1[i][j] + matrix2[i][j]
            row.append(sum_element)
        result.append(row)
    return result

def print_matrix(matrix):
    print("The resulting matrix after addition is:")
    for row in matrix:
        print(row)

# Create the first matrix
print("Enter elements for the first matrix:")
matrix1 = create_matrix()

# Create the second matrix
print("\nEnter elements for the second matrix:")
matrix2 = create_matrix()

# Add the matrices
result_matrix = add_matrices(matrix1, matrix2)

# Print the result
print_matrix(result_matrix)
