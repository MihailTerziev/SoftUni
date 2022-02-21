from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

gifts = {
    "Bicycle": 0,
    "Doll": 0,
    "Teddy bear": 0,
    "Wooden train": 0
}

while materials and magic_levels:
    last_box = materials.pop()
    first_magic = magic_levels.popleft()
    total_magic_level = last_box * first_magic

    if total_magic_level == 150:
        gifts["Doll"] += 1
    elif total_magic_level == 250:
        gifts["Wooden train"] += 1
    elif total_magic_level == 300:
        gifts["Teddy bear"] += 1
    elif total_magic_level == 400:
        gifts["Bicycle"] += 1
    else:
        if total_magic_level < 0:
            materials.append(last_box + first_magic)
        elif total_magic_level > 0:
            materials.append(last_box + 15)
        else:
            if last_box == 0 and first_magic == 0:
                continue
            if last_box == 0:
                magic_levels.appendleft(first_magic)
            if first_magic == 0:
                materials.append(last_box)

if (gifts["Doll"] > 0 and gifts["Wooden train"] > 0) or (gifts["Teddy bear"] > 0 and gifts["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for gift, count in gifts.items():
    if count > 0:
        print(f"{gift}: {count}")
