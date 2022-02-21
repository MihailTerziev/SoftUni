def fill_the_box(*args):
    height, length, width, *boxes = args
    area = height * length * width

    for box in boxes:
        if box == "Finish":
            break
        area -= box

    if area > 0:
        return f"There is free space in the box. You could put {area} more cubes."
    return f"No more free space! You have {abs(area)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
