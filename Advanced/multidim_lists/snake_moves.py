rows, cols = [int(x) for x in input().split()]
snake = input()
idx = 0

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(snake[idx % len(snake)])
        idx += 1

    if i % 2 == 0:
        print(*row, sep='')
    else:
        print(*reversed(row), sep='')
