def is_knight(row: int, col: int, mat: list) -> bool:
    return mat[row][col] == 'K'


def is_inside(row: int, col: int, size: int) -> bool:
    return 0 <= row < size and 0 <= col < size


def get_attack_counter(row: int, col: int, mat: list) -> int:
    result = 0

    if is_inside(row-2, col-1, len(mat)) and is_knight(row-2, col-1, mat):
        result += 1
    if is_inside(row-2, col+1, len(mat)) and is_knight(row-2, col+1, mat):
        result += 1
    if is_inside(row-1, col-2, len(mat)) and is_knight(row-1, col-2, mat):
        result += 1
    if is_inside(row-1, col+2, len(mat)) and is_knight(row-1, col+2, mat):
        result += 1
    if is_inside(row+2, col-1, len(mat)) and is_knight(row+2, col-1, mat):
        result += 1
    if is_inside(row+2, col+1, len(mat)) and is_knight(row+2, col+1, mat):
        result += 1
    if is_inside(row+1, col-2, len(mat)) and is_knight(row+1, col-2, mat):
        result += 1
    if is_inside(row+1, col+2, len(mat)) and is_knight(row+1, col+2, mat):
        result += 1

    return result


n = int(input())
matrix = []
removed_knights = 0

for _ in range(n):
    matrix.append(list(input()))

while True:
    table = {}

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '0':
                continue

            counter = get_attack_counter(i, j, matrix)
            if counter:
                table[(i, j)] = counter

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for position, count in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = position[0]
            knight_col = position[1]

    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
