n = int(input())
matrix = []
s = 0

for i in range(n):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)
    s += matrix[i][i]

print(s)
