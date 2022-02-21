from collections import deque

kids = deque(input().split())
n = int(input())

while len(kids) > 1:
    kids.rotate(-n)  # if -n rotate to left, if +n rotate clockwise, n-times
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.popleft()}")
