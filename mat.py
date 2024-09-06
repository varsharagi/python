#Write a program that reads an M x N matrix and prints the perimeter of the matrix.
#Note
#The perimeter of the matrix is defined as the sum of all the elements on the four edges of the matrix.
#Input
#The first line of input contains space-separated integers representing M and N respectively.
#The next M lines of input contain N space-separated integers representing the matri

#Code:

def calculate_perimeter(matrix):
    if not matrix:
        return 0
    M = len(matrix)
    N = len(matrix[0])
    perimeter_sum = 0
    
    # Add the top row
    perimeter_sum += sum(matrix[0])
    
    # Add the bottom row if there are multiple rows
    if M > 1:
        perimeter_sum += sum(matrix[-1])
    
    # Add the left column (excluding corners if M > 1)
    for i in range(1, M - 1):
        perimeter_sum += matrix[i][0]
    
    # Add the right column (excluding corners if N > 1)
    if N > 1:
        for i in range(1, M - 1):
            perimeter_sum += matrix[i][-1]
    
    return perimeter_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read matrix dimensions
    M, N = map(int, data[0].split())
    
    # Read matrix data
    matrix = []
    for i in range(1, M + 1):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    # Calculate perimeter
    perimeter = calculate_perimeter(matrix)
    print(perimeter)

# Correct __name__ check
if __name__ == "__main__":
    main()
