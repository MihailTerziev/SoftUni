rows, cols = [int(x) for x in input().split(", ")]
s = 0
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    if len(row) == cols:
        s += sum(row)
        matrix.append(row)

print(s)
print(matrix)

for i in range(rows):
    matrix.append([])
    for _ in range(cols):
        n = int(input())
        matrix[i].append(n)

print(*matrix, sep=", ")
