rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    row = input().split()
    matrix.append(row)

command = input()

while not command == "END":
    args = command.split()

    if len(args) == 5 and args[0] == "swap" and 0 <= int(args[1]) <= rows-1 >= int(args[3]) >= 0 and 0 <= int(args[2]) <= cols-1 >= int(args[4]) >= 0:
        row1, col1, row2, col2 = [int(x) for x in args[1:]]
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for i in range(rows):
            for j in range(cols):
                print(matrix[i][j], end=' ')
            print()
    else:
        print("Invalid input!")

    command = input()
