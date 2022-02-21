n = int(input())
odd_set = set()
even_set = set()

for i in range(n):
    name = input()
    s = 0

    for ch in name:
        s += ord(ch)

    s = int(s / (i + 1))

    if s % 2 == 0:
        even_set.add(s)
    else:
        odd_set.add(s)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)
if odd_set_sum == even_set_sum:
    print(", ".join([str(x) for x in odd_set.union(even_set)]))
elif odd_set_sum > even_set_sum:
    print(", ".join([str(x) for x in odd_set.difference(even_set)]))
else:
    print(", ".join([str(x) for x in odd_set.symmetric_difference(even_set)]))
