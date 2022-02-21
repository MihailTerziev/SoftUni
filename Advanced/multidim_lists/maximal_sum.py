import sys

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

max_sum = -sys.maxsize
max_sub_matrix = []

for i in range(rows-2):
    for j in range(cols-2):
        sub_matrix = [matrix[i][j], matrix[i][j+1], matrix[i][j+2],
                      matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2],
                      matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()

print(f"Sum = {max_sum}")
print(max_sub_matrix[0], max_sub_matrix[1], max_sub_matrix[2])
print(max_sub_matrix[3], max_sub_matrix[4], max_sub_matrix[5])
print(max_sub_matrix[6], max_sub_matrix[7], max_sub_matrix[8])
