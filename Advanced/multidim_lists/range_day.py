def get_next_position(d: str, row: int, col: int, s: int):
    if d == "up":
        return row - s, col
    if d == "down":
        return row + s, col
    if d == "left":
        return row, col - s
    if d == "right":
        return row, col + s


def is_outside(row: int, col: int, size: int):
    return row < 0 or col < 0 or row >= size or col >= size


n = 5
matrix = []
shooter_x, shooter_y = 0, 0
total_targets = 0

for i in range(n):
    elements = input().split()
    matrix.append(elements)
    for j in range(n):
        if elements[j] == 'A':
            shooter_x = i
            shooter_y = j
        elif elements[j] == 'x':
            total_targets += 1

n = int(input())
shot_targets = []
hit_targets = total_targets

for _ in range(n):
    args = input().split()
    command, direction = args[0], args[1]

    if command == "move":
        steps = int(args[2])
        next_row, next_col = get_next_position(direction, shooter_x, shooter_y, steps)

        if is_outside(next_row, next_col, n) or matrix[next_row][next_col] != '.':
            continue

        matrix[shooter_x][shooter_y] = '.'
        shooter_x, shooter_y = next_row, next_col
        matrix[shooter_x][shooter_y] = 'A'

    elif command == "shoot":
        bullet_x, bullet_y = shooter_x, shooter_y

        while True:
            bullet_x, bullet_y = get_next_position(direction, bullet_x, bullet_y, 1)

            if is_outside(bullet_x, bullet_y, 5):
                break

            if matrix[bullet_x][bullet_y] == 'x':
                matrix[bullet_x][bullet_y] = '.'
                hit_targets -= 1
                shot_targets.append([bullet_x, bullet_y])
                break

        if hit_targets == 0:
            break

if hit_targets == 0:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {hit_targets} targets left.")

print(*shot_targets, sep="\n")
