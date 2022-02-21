def even_odd(*args):
    *numbers, command = args

    parity = 0 if command == "even" else 1
    output = [x for x in numbers if x % 2 == parity]
    return output


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
