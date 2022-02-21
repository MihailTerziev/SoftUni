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


presents = int(input())
size = int(input())
hood = []
santa_x, santa_y = 0, 0
nice_kids = 0

for i in range(size):
    elements = input().split()
    hood.append(elements)
    for j in range(size):
        if elements[j] == 'S':
            santa_x = i
            santa_y = j
        elif elements[j] == 'V':
            nice_kids += 1

command = input()
left_nice_kids = nice_kids

while not command == "Christmas morning":
    hood[santa_x][santa_y] = '-'
    next_row, next_col = get_next_position(command, santa_x, santa_y)

    if is_outside(next_row, next_col, size):
        command = input()
        continue

    santa_x, santa_y = next_row, next_col

    if hood[santa_x][santa_y] == 'V':
        presents -= 1
        left_nice_kids -= 1
    elif hood[santa_x][santa_y] == 'C':
        if hood[santa_x-1][santa_y] == 'V' and presents:
            presents -= 1
            left_nice_kids -= 1
            hood[santa_x-1][santa_y] = '-'
        elif hood[santa_x-1][santa_y] == 'X' and presents:
            presents -= 1
            hood[santa_x-1][santa_y] = '-'

        if hood[santa_x+1][santa_y] == 'V' and presents:
            presents -= 1
            left_nice_kids -= 1
            hood[santa_x+1][santa_y] = '-'
        elif hood[santa_x+1][santa_y] == 'X' and presents:
            presents -= 1
            hood[santa_x+1][santa_y] = '-'

        if hood[santa_x][santa_y-1] == 'V' and presents:
            presents -= 1
            left_nice_kids -= 1
            hood[santa_x][santa_y-1] = '-'
        elif hood[santa_x][santa_y-1] == 'X' and presents:
            presents -= 1
            hood[santa_x][santa_y-1] = '-'

        if hood[santa_x][santa_y+1] == 'V' and presents:
            presents -= 1
            left_nice_kids -= 1
            hood[santa_x][santa_y+1] = '-'
        elif hood[santa_x][santa_y+1] == 'X' and presents:
            presents -= 1
            hood[santa_x][santa_y+1] = '-'

    hood[santa_x][santa_y] = 'S'
    if presents == 0 or left_nice_kids == 0:
        break

    command = input()

if presents == 0 and left_nice_kids > 0:
    print("Santa ran out of presents!")

for street in hood:
    print(*street, sep=' ')

if left_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {left_nice_kids} nice kid/s.")
