s = input()
open_brackets = []
balanced = True

for ch in s:
    if ch in "([{":
        open_brackets.append(ch)
    elif not open_brackets:
        balanced = False
        break
    else:
        last_bracket = open_brackets.pop()
        if f"{last_bracket}{ch}" not in "()[]{}":
            balanced = False
            break

if balanced and not open_brackets:  # not stack = []
    print("YES")
else:
    print("NO")
