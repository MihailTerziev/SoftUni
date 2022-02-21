from collections import deque

# searched_words = {
#     1: ['r', 'o,' 's', 'e'],
#     2: ['t', 'u', 'l', 'i', 'p'],
#     3: ['l', 'o', 't', 'u', 's'],
#     4: ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l']
# }

searched_words = {
    1: ["rose"],
    2: ["tulip"],
    3: ["lotus"],
    4: ["daffodil"]
}

flower_dict = {
    1: "rose",
    2: "tulip",
    3: "lotus",
    4: "daffodil"
}
vowels = deque(input().split())
consonants = input().split()
is_found = False
searched_index = 0

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for index, word in searched_words.items():
        for flower in word:
            if current_vowel in flower:
                flower = flower.replace(current_vowel, '')
            if current_consonant in flower:
                flower = flower.replace(current_consonant, '')

            word.clear()
            word.append(flower)

        if word[0] == '':
            is_found = True
            searched_index = index
            break

    if is_found:
        break

if is_found:
    print(f"Word found: {flower_dict[searched_index]}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")