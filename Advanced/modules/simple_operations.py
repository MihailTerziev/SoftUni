from simple_operations.helper import operation_mapper

data = input().split()
a, sign, b = float(data[0]), data[1], float(data[2])

print(f"{operation_mapper[sign](a, b):.2f}")
