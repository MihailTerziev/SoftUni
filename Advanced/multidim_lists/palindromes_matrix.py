rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[i].append(chr(i+97) + chr(i+j+97) + chr(i+97))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
