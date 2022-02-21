numbers = (float(n) for n in input().split())
occ = {}

for n in numbers:
    if n not in occ:
        occ[n] = 0
    occ[n] += 1

for key, value in occ.items():
    print(f"{key:.1f} - {value} times")
