n = int(input())
matrix = []
s1 = 0
s2 = 0
primary = []
second = []

for i in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

    primary.append(matrix[i][i])
    s1 += matrix[i][i]

    second.append(matrix[i][n-i-1])
    s2 += matrix[i][n-i-1]

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {s1}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second])}. Sum: {s2}")
