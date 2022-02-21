symbols = ['-', ',', '.', '!', '?']

with open("text.txt", 'r') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = line.strip()  # remove \n
            result = ' '.join(reversed(line.split()))  # reverse string

            for char in symbols:
                result = result.replace(char, '@')  # replace with @

            print(result)
