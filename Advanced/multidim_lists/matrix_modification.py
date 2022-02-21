n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

command = input()

while not command == "END":
    args = command.split()
    row, col, value = [int(x) for x in args[1:]]

    if row < 0 or col < 0 or row >= n or col >= n:
        print("Invalid coordinates")
        command = input()
        continue

    if args[0] == "Add":
        matrix[row][col] += value
    elif args[0] == "Subtract":
        matrix[row][col] -= value

    command = input()

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
