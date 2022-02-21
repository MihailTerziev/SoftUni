n, m = [int(x) for x in input().split()]
a = set()
b = set()

for _ in range(n):
    a.add(input())

for _ in range(m):
    b.add(input())

print("\n".join(a.intersection(b)))
