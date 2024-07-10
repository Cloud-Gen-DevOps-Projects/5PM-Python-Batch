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

def print_matrix(matrix):
    print("The 3x3 matrix is:")
    for row in matrix:
        print(row)

# Create the matrix
matrix = create_matrix()

# Print the matrix
print_matrix(matrix)
