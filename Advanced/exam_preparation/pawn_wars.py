matrix = []
black_x, black_y = 0, 0
white_x, white_y = 0, 0

board = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
]

for x in range(8):
    row = input().split()
    matrix.append(row)
    for y in range(len(row)):
        if row[y] == 'b':
            black_x = x
            black_y = y
        if row[y] == 'w':
            white_x = x
            white_y = y

while True:
    if white_x == 0:
        print(f"Game over! White pawn is promoted to a queen at {board[0][white_y]}.")
        break

    if not white_x == 0 and not white_y == 7 and matrix[white_x - 1][white_y + 1] == matrix[black_x][black_y]:
        white_x, white_y = black_x, black_y
        print(f"Game over! White win, capture on {board[white_x][white_y]}.")
        break

    if not white_x == 0 and not white_y == 0 and matrix[white_x - 1][white_y - 1] == matrix[black_x][black_y]:
        white_x, white_y = black_x, black_y
        print(f"Game over! White win, capture on {board[white_x][white_y]}.")
        break

    white_x, white_y = white_x - 1, white_y

    if black_x == 7:
        print(f"Game over! Black pawn is promoted to a queen at {board[7][black_y]}.")
        break

    if not black_x == 7 and not black_y == 7 and matrix[black_x + 1][black_y + 1] == matrix[white_x][white_y]:
        black_x, black_y = white_x, white_y
        print(f"Game over! Black win, capture on {board[black_x][black_y]}.")
        break

    if not black_x == 7 and not black_y == 0 and matrix[black_x + 1][black_y - 1] == matrix[white_x][white_y]:
        black_x, black_y = white_x, white_y
        print(f"Game over! Black win, capture on {board[black_x][black_y]}.")
        break

    black_x, black_y = black_x + 1, black_y
