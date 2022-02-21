set_a = {int(x) for x in input().split()}
set_b = {int(x) for x in input().split()}
n = int(input())

for _ in range(n):
    args = input().split()
    command, s = args[0], args[1]
    if command == "Add":
        if s == "First":
            add_set = {int(x) for x in args[2:]}
            set_a.update(add_set)
        elif s == "Second":
            [set_b.add(int(x)) for x in args[2:]]
    elif command == "Remove":
        if s == "First":
            set_a = set_a.difference([int(x) for x in args[2:]])
        else:
            set_b = set_b.difference([int(x) for x in args[2:]])
    elif command == "Check" and s == "Subset":
        print(set_a.issubset(set_b) or set_b.issubset(set_a))

print(*sorted(set_a), sep=", ")
print(*sorted(set_b), sep=", ")
