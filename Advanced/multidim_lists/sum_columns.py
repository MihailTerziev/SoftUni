rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for j in range(cols):
    s = 0
    for i in range(rows):
        s += matrix[i][j]
    print(s)
