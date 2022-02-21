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
wonderland = []
alice_x, alice_y = 0, 0
tea_sum = 0

for x in range(n):
    row = input().split()
    wonderland.append(row)
    for y in range(n):
        if row[y] == 'A':
            alice_x = x
            alice_y = y

while True:
    direction = input()

    if not wonderland[alice_x][alice_y] == '*':
        wonderland[alice_x][alice_y] = '*'

    alice_x, alice_y = get_next_position(direction, alice_x, alice_y)

    if is_outside(alice_x, alice_y, n):
        print("Alice didn't make it to the tea party.")
        break

    if wonderland[alice_x][alice_y] == 'R':
        wonderland[alice_x][alice_y] = '*'
        print("Alice didn't make it to the tea party.")
        break

    if wonderland[alice_x][alice_y] not in ".*":
        tea_sum += int(wonderland[alice_x][alice_y])
        wonderland[alice_x][alice_y] = '*'

    if tea_sum >= 10:
        print("She did it! She went to the party.")
        break

for row in wonderland:
    print(*row, sep=' ')
