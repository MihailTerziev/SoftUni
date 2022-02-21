def args_length(*args):
    counter = 0
    for _ in args:
        counter += 1
    return counter


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
