from os import path, remove

line = input()

while not line == "End":
    args = line.split('-')
    command, file_name = args[0], args[1]

    if command == "Create":
        open(file_name, 'w').close()

    elif command == "Add":
        content = args[2]
        with open(file_name, 'a') as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_str, new_str = args[2], args[3]
        if path.exists(file_name):
            with open(file_name, 'r+') as file:
                result = file.read()  # get file content
                file.seek(0)          # return cursor to the beginning of file
                file.truncate()       # clean file content
                file.write(result.replace(old_str, new_str))
        else:
            print("An error occurred")

    elif command == "Delete":
        if path.exists(file_name):
            remove(file_name)
        else:
            print("An error occurred")

    line = input()
