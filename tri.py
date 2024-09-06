#Yash is solving a matrix problem as part of his entrance exam preparation.
#In that matrix problem, there is a square matrix of size N x N. Yash needs to calculate the sum of the upper and lower triangular
#elements of the matrix. Help Yash solve the given matrix problem.
#Write a program that reads the NX N matrix and prints the sum of the upper and lower triangular elements.
#Note
#The upper triangle consists of elements on the anti- diagonal and above on it.
#The lower triangle consists of elements on the anti- diagonal and below it.

#Code:
def calculate_upper_lower_triangular_sum(matrix, N):
    upper_sum = 0
    lower_sum = 0

    for i in range(N):
        for j in range(N):
            # Anti-diagonal index for element (i, j)
            anti_diag_index = i + j
            
            if j <= N - 1 - i:
                upper_sum += matrix[i][j]
            if j >= N - 1 - i:
                lower_sum += matrix[i][j]

    return upper_sum, lower_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read matrix size N
    N = int(data[0])
    
    # Read matrix data
    matrix = []
    for i in range(1, N + 1):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    # Calculate sums of upper and lower triangular parts
    upper_sum, lower_sum = calculate_upper_lower_triangular_sum(matrix, N)
    
    # Print the results
    print(f"Sum of the upper triangular elements: {upper_sum}")
    print(f"Sum of the lower triangular elements: {lower_sum}")

# Correct __name__ check
if __name__ == "__main__":
    main()
