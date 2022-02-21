try:
    with open("numbers.txt") as file:
        print(sum([int(line) for line in file.readlines()]))
except FileNotFoundError:
    print("File not found")

# file.read().split() -> 1 2 3 4 5 -> [1, 2, 3, 4, 5]
# [print(line , end='') for line in file.readlines()]
