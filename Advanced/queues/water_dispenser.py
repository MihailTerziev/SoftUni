from collections import deque

line = deque()
liters = int(input())
name = input()

while name != "Start":
    line.append(name)
    name = input()

command = input()

while command != "End":
    args = command.split()
    if len(args) == 1:
        water = int(args[0])
        person = line.popleft()
        if liters >= water:
            liters -= water
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    else:
        water = int(args[1])
        liters += water

    command = input()

print(f"{liters} liters left")
