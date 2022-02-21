lines = []
symbols = ["-", ",", ".", "!", "?", "'", '"']

with open("text.txt") as file:
    for line in file:
        lines.append(line.strip())  # get lines from text.txt

with open("output.txt", 'w') as file:
    for row_number, line in enumerate(lines, 1):  # row_number starts from 1
        symbols_counter = 0
        letters_counter = 0

        for letter in line:
            if letter in symbols:
                symbols_counter += 1
            if letter.isalpha():
                letters_counter += 1

        result = f"Line {row_number}: " + line + f" ({letters_counter})({symbols_counter})\n"
        file.write(result)
