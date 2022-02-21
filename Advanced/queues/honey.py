from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

while bees and nectars:
    bee = bees[0]
    nectar = nectars.pop()

    if bee > nectar:
        continue

    bees.popleft()
    symbol = symbols.popleft()

    if symbol == '+':
        total_honey += abs(bee + nectar)
    elif symbol == '*':
        total_honey += abs(bee * nectar)
    elif symbol == '-':
        total_honey += abs(bee - nectar)
    elif symbol == '/' and nectar > 0:
        total_honey += abs(bee / nectar)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")

if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
