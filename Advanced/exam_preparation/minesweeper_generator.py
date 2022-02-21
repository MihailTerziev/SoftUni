def count_bombs_around(matrix: list, row: int, col: int, size: int) -> int:
    counter = 0

    if not row == 0 and matrix[row - 1][col] == '*':
        counter += 1
    if not row == size - 1 and matrix[row + 1][col] == '*':
        counter += 1
    if not col == 0 and matrix[row][col - 1] == '*':
        counter += 1
    if not col == size - 1 and matrix[row][col + 1] == '*':
        counter += 1
    if not row == 0 and not col == size - 1 and matrix[row - 1][col + 1] == '*':
        counter += 1
    if not row == 0 and not col == 0 and matrix[row - 1][col - 1] == '*':
        counter += 1
    if not row == size - 1 and not col == size - 1 and matrix[row + 1][col + 1] == '*':
        counter += 1
    if not row == size - 1 and not col == 0 and matrix[row + 1][col - 1] == '*':
        counter += 1

    return counter


def print_matrix(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
bombs = int(input())
_matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(bombs):
    bomb_x, bomb_y = eval(input())
    _matrix[bomb_x][bomb_y] = '*'

for x in range(n):
    for y in range(n):
        if not _matrix[x][y] == '*':
            _matrix[x][y] = count_bombs_around(_matrix, x, y, n)

print_matrix(_matrix)
