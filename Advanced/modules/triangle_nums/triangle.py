def print_up_part(number: int):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()


def print_down_part(number: int):
    for i in range(number-1, 0, -1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()


def print_triangle(number: int):
    print_up_part(number)
    print_down_part(number)
