from collections import deque


def math_operations(*args, **kwargs):
    args_queue = deque(args)
    counter = 0

    while args_queue:
        number = args_queue.popleft()
        counter += 1

        if counter == 5:
            counter = 1

        if counter == 1:
            kwargs['a'] += number
        elif counter == 2:
            kwargs['s'] -= number
        elif counter == 3 and not number == 0:
            kwargs['d'] /= number
        elif counter == 4:
            kwargs['m'] *= number

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
