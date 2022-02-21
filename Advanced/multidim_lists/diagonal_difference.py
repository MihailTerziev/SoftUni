n = int(input())
matrix = []
s1 = 0
s2 = 0

for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    s1 += matrix[i][i]
    s2 += matrix[i][n-i-1]

print(abs(s1 - s2))
