from math import floor


def get_next_position(direction: str, row: int, col: int):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


def is_outside(row: int, col: int, size: int):
    return row < 0 or col < 0 or row >= size or col >= size


def correct_path(direction: str, row: int, col: int, size: int):
    if direction == "up":
        return size - 1, col
    if direction == "down":
        return 0, col
    if direction == "left":
        return row, size - 1
    if direction == "right":
        return row, 0


n = int(input())
matrix = []
coins = 0
player_x, player_y = 0, 0
player_path = []

for x in range(n):
    _row = input().split()
    matrix.append(_row)
    for y in range(n):
        if _row[y] == 'P':
            player_x = x
            player_y = y

while True:
    command = input()

    player_path.append([player_x, player_y])

    if not matrix[player_x][player_y] == '0':
        matrix[player_x][player_y] = '0'

    player_x, player_y = get_next_position(command, player_x, player_y)

    if is_outside(player_x, player_y, n):
        player_x, player_y = correct_path(command, player_x, player_y, n)

    if matrix[player_x][player_y] == 'X':
        player_path.append([player_x, player_y])
        print(f"Game over! You've collected {floor(coins / 2)} coins.")
        break

    coins += int(matrix[player_x][player_y])

    if coins >= 100:
        player_path.append([player_x, player_y])
        print(f"You won! You've collected {coins} coins.")
        break

print("Your path:")
print(*player_path, sep='\n')
