text = input()
letters = {}

for ch in text:
    if ch not in letters:
        letters[ch] = 0
    letters[ch] += 1

sorted_letters = sorted(letters.items(), key=lambda x: x[0])

for pair in sorted_letters:
    ch, occ = pair
    print(f"{ch}: {occ} time/s")
