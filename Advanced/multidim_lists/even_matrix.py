rows = int(input())
matrix = []

for i in range(rows):
    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)
    matrix[i] = [x for x in matrix[i] if x % 2 == 0]

print(matrix)
