from collections import deque


def detonate_matrix(matrix: list, row: int, col: int, size: int) -> list:
    value = matrix[row][col]
    matrix[row][col] -= value

    if not row == 0 and matrix[row - 1][col] > 0:
        matrix[row - 1][col] -= value
    if not row == size - 1 and matrix[row + 1][col] > 0:
        matrix[row + 1][col] -= value
    if not col == 0 and matrix[row][col - 1] > 0:
        matrix[row][col - 1] -= value
    if not col == size - 1 and matrix[row][col + 1] > 0:
        matrix[row][col + 1] -= value
    if not row == 0 and not col == size - 1 and matrix[row - 1][col + 1] > 0:
        matrix[row - 1][col + 1] -= value
    if not row == 0 and not col == 0 and matrix[row - 1][col - 1] > 0:
        matrix[row - 1][col - 1] -= value
    if not row == size - 1 and not col == size - 1 and matrix[row + 1][col + 1] > 0:
        matrix[row + 1][col + 1] -= value
    if not row == size - 1 and not col == 0 and matrix[row + 1][col - 1] > 0:
        matrix[row + 1][col - 1] -= value

    return matrix


def print_matrix(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
_matrix = []
alive_cells = 0
alive_cells_sum = 0

for _ in range(n):
    _matrix.append([int(x) for x in input().split()])

bombs = deque(input().split())

while bombs:
    current_bomb = bombs.popleft()
    bomb_x, bomb_y = [int(x) for x in current_bomb.split(',')]

    if _matrix[bomb_x][bomb_y] <= 0:
        continue

    _matrix = detonate_matrix(_matrix, bomb_x, bomb_y, n)

for x in range(n):
    for y in range(n):
        if _matrix[x][y] > 0:
            alive_cells += 1
            alive_cells_sum += _matrix[x][y]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
print_matrix(_matrix)
