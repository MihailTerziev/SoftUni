from collections import deque
import math

expression = input().split()
queue = deque()

# operations = {
#     "*": lambda a, b: a * b,
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a * b,
#     "/": lambda a, b: a * b
# }

for el in expression:
    if el in "*+-/":
        while len(queue) > 1:
            first_num = queue.popleft()
            second_num = queue.popleft()
            if el == '*':
                queue.appendleft(first_num * second_num)
            elif el == '+':
                queue.appendleft(first_num + second_num)
            elif el == '-':
                queue.appendleft(first_num - second_num)
            elif el == '/':
                queue.appendleft(math.floor(first_num / second_num))

            # result = operations[element](first_num, second_num)
            # queue.appendleft(result)
    else:
        queue.append(int(el))

print(queue.popleft())
