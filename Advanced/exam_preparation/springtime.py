def start_spring(**kwargs):
    rev_dict = {}
    for key, value in kwargs.items():
        if value not in rev_dict:
            rev_dict[value] = []
        rev_dict[value].append(key)

    output = ""
    sorted_flowers = sorted(rev_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for name, quantities in sorted_flowers:
        sorted_quantities = sorted(quantities)
        output += f"{name}:\n"
        for item in sorted_quantities:
            output += f"-{item}\n"
    output = output.strip()
    return output


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",
                   }
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",
                   }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"
                   }
print(start_spring(**example_objects))
