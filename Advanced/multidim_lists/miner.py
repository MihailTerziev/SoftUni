from collections import deque


def get_next_position(direction: str, row: int, col: int):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


def is_outside(row: int, col: int, s: int):
    return row < 0 or col < 0 or row >= s or col >= s


n = int(input())
commands = deque(input().split())
mine = []
miner_x, miner_y = 0, 0
collected_coal = 0
flag = True

for x in range(n):
    _row = input().split()
    mine.append(_row)
    for y in range(n):
        if _row[y] == 's':
            miner_x = x
            miner_y = y
        if _row[y] == 'c':
            collected_coal += 1

while commands:
    current_command = commands.popleft()

    if not mine[miner_x][miner_y] == '*':
        mine[miner_x][miner_y] = '*'

    next_x, next_y = get_next_position(current_command, miner_x, miner_y)

    if is_outside(next_x, next_y, n):
        continue
    else:
        miner_x, miner_y = next_x, next_y

    if mine[miner_x][miner_y] == 'c':
        collected_coal -= 1

    if collected_coal == 0:
        flag = False
        print(f"You collected all coal! ({miner_x}, {miner_y})")
        break

    if mine[miner_x][miner_y] == 'e':
        flag = False
        print(f"Game over! ({miner_x}, {miner_y})")
        break

if flag:
    print(f"{collected_coal} pieces of coal left. ({miner_x}, {miner_y})")
