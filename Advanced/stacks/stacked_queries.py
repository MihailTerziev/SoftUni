stack = []
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]
    if command == '1':
        num = int(line[1])
        stack.append(num)
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))

while stack:
    element = stack.pop()          # how to print without the last ','
    if stack:
        print(element, end=", ")
    else:
        print(element)
