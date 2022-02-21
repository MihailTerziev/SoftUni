import os

try:
    file = open("example_file.txt")
    print("File found")
except FileNotFoundError:
    print("File no found")

if os.path.exists("example_file.txt"):
    print("File found")  # check if file exists but in the current directory only
else:
    print("File not found")
