import re

searched_words = []

with open("words.txt") as file:
    searched_words = file.read().split()

words_counter = {}

with open("input.txt") as file:
    text = file.read()
    for word in searched_words:
        pattern = fr"\b{word}\b"
        count = len(re.findall(pattern, text, re.IGNORECASE))
        words_counter[word] = count

sorted_words = sorted(words_counter.items(), key=lambda x: -x[1])

with open("output.txt", 'a') as file:
    for key, value in sorted_words:
        file.writelines(f"{key} - {value}\n")
