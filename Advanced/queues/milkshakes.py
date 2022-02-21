from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milks = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while chocolates and milks and milkshakes < 5:
    chocolate = chocolates.pop()
    milk_cup = milks.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue

    if chocolate <= 0:
        milks.appendleft(milk_cup)
        continue

    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        milks.append(milk_cup)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if milks:
    print(f"Milk: {', '.join([str(x) for x in milks])}")
else:
    print("Milk: empty")
