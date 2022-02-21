from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    station = [int(n) for n in input().split()]
    pumps.append(station)

for attempt in range(n):
    tank = 0
    failed = False
    for fuel, distance in pumps:
        tank += fuel
        if tank < distance:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        pumps.append(pumps.popleft())  # pump.rotate(-1)
    else:
        print(attempt)
        break
