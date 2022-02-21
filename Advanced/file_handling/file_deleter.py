import os

if os.path.exists("python.txt"):
    os.remove("python.txt")
else:
    print("File already deleted!")
