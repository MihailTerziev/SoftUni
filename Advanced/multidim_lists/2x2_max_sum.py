import sys

rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

max_sum = -sys.maxsize
max_submatrix = []

for i in range(rows-1):
    for j in range(cols-1):
        submatrix = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]

        current_sum = sum(submatrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_submatrix = submatrix.copy()

print(max_submatrix[0], max_submatrix[1])
print(max_submatrix[2], max_submatrix[3])
print(max_sum)
