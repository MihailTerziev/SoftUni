from collections import deque

quantity = int(input())
integers = deque([int(n) for n in input().split()])

print(max(integers))

while integers:
    first_num = integers[0]
    if quantity - first_num >= 0:
        quantity -= first_num
        integers.popleft()
    else:
        break

if integers:
    print(f"Orders left: {' '.join([str(n) for n in integers])}")
else:
    print("Orders complete")
