from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]
bomb_pouch = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
datura_bombs_value = 40
cherry_bombs_value = 60
smoke_decoy_bombs_value = 120
pouch_is_filled = False

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    if current_effect + current_casing == cherry_bombs_value:
        bomb_pouch["Cherry Bombs"] += 1
    elif current_effect + current_casing == datura_bombs_value:
        bomb_pouch["Datura Bombs"] += 1
    elif current_effect + current_casing == smoke_decoy_bombs_value:
        bomb_pouch["Smoke Decoy Bombs"] += 1
    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)
        continue

    for bomb_count in bomb_pouch.values():
        if bomb_count >= 3:
            pouch_is_filled = True
        else:
            pouch_is_filled = False
            break

    if pouch_is_filled:
        break

if pouch_is_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for bomb_type, count in bomb_pouch.items():
    print(f"{bomb_type}: {count}")
