def sum_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def mul_nums(a, b):
    return a * b


def div_nums(a, b):
    while True:
        try:
            return a / b
        except ZeroDivisionError:
            print("b can't be 0!")
            b = int(input("Enter b again: "))


def pow_nums(a, b):
    return a ** b


operation_mapper = {
    '+': sum_nums,
    '-': sub_nums,
    '*': mul_nums,
    '/': div_nums,
    '^': pow_nums
}
