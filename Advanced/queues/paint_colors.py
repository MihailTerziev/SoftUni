from collections import deque

strings = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
collected_colors = list()

while strings:
    first = strings.popleft()
    last = strings.pop() if strings else ''

    result = first + last
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = last + first
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        strings.insert(len(strings) // 2, first)

    if last:
        strings.insert(len(strings) // 2, last)

result = []
required_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

for color in collected_colors:
    if color in main_colors:
        result.append(color)
    else:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in collected_colors:
                is_valid = False
                break

        if is_valid:
            result.append(color)

print(result)
