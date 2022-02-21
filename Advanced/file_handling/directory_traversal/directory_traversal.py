from os import path, listdir


def traverse_dir(file_path, ext_dict):
    for element in listdir(file_path):
        if path.isdir(path.join(file_path, element)):
            traverse_dir(path.join(file_path, element), ext_dict)
        else:
            extension = element.split('.')[-1]
            if extension not in ext_dict:
                ext_dict[extension] = []
            ext_dict[extension].append(element)


with open("report.txt", 'w') as file:
    files_ext = {}
    traverse_dir('.', files_ext)

    for ext, files in sorted(files_ext.items()):
        file.write(f".{ext}\n")
        for file_name in files:
            file.write(f"- - - {file_name}\n")
