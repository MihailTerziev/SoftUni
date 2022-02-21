stack = [int(n) for n in input().split()]
rack = int(input())
counter = 1
current_rack = rack

while stack:
    current_cloth = stack[-1]
    if current_rack >= current_cloth:
        stack.pop()
        current_rack -= current_cloth
    else:
        counter += 1
        current_rack = rack

print(counter)
