import sys


def move_up(row: int, col: int):
    return row - 1, col


def move_down(row: int, col: int):
    return row + 1, col


def move_left(row: int, col: int):
    return row, col - 1


def move_right(row: int, col: int):
    return row, col + 1


n = int(input())
matrix = []
bunny_row, bunny_col = 0, 0
best_score = -sys.maxsize  # float("-inf")
best_direction = ""
best_path = []

directions = {
    "left": move_left,  # reference to the function
    "right": move_right,
    "up": move_up,
    "down": move_down
}

for i in range(n):
    row = input().split()
    matrix.append(row)

    for j in range(n):
        if row[j] == 'B':
            bunny_row = i
            bunny_col = j

for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    path = []

    while True:
        current_row, current_col = step(current_row, current_col)

        if current_row < 0 or current_row >= n or current_col < 0 or current_col >= n or matrix[current_row][current_col] == 'X':
            break

        path.append([current_row, current_col])
        current_score += int(matrix[current_row][current_col])

    if current_score > best_score and path:
        best_score = current_score
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep="\n")
print(best_score)
