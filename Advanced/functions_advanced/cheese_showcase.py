def sorting_cheeses(**kwargs):
    output = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for name, quantities in sorted_cheeses:
        sorted_quantities = sorted(quantities, reverse=True)
        output += name + "\n"
        output += "\n".join([str(x) for x in sorted_quantities]) + "\n"
    output = output.strip()
    return output


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
