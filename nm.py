#Write a program that reads an Nx N matrix and checks if it is a unique matrix or not.
#4
#5
#6-
#Note
#7
#8-
#A Unique Matrix is a matrix in which every row and column contains all integers from 1 to N.
#9
#10-
#11
#12
#13 n-
#Input
#The first line of input contains an integer representing N.
#14 che
#15 mai
#The next N lines of input contain N space-separated integers representing the matrix.
#16 tra
#17

#Code:
def is_unique_matrix(matrix, N):
    required_set = set(range(1, N + 1)) 
    for row in matrix:
        if set(row) != required_set:
            return False
    for col in range(N):
        col_set = set(matrix[row][col] for row in range(N))
        if col_set != required_set:
            return False

    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])
    
    matrix = []
    for i in range(1, N + 1):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    if is_unique_matrix(matrix, N):
        print("The matrix is unique.")
    else:
        print("The matrix is not unique.")

if __name__ == "__main__":
    main()
