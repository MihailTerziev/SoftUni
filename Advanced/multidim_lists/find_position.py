n = int(input())
matrix = []

for _ in range(n):
    symbols = [ch for ch in input()]
    matrix.append(symbols)

symbol = input()
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
