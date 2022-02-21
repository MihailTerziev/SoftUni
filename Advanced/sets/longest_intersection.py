def gen_set(range_info: str) -> set:
    s, e = [int(x) for x in range_info.split(',')]
    return set(range(s, e+1))


n = int(input())
biggest_intersection = set()

for _ in range(n):
    first_start, second_start = input().split('-')
    a = gen_set(first_start)
    b = gen_set(second_start)

    current_intersection = a.intersection(b)
    if len(current_intersection) > len(biggest_intersection):
        biggest_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in biggest_intersection])}] with length {len(biggest_intersection)}")
