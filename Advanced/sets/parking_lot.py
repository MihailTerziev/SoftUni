n = int(input())
parking = set()

for _ in range(n):
    command, car_licence = input().split(", ")
    if command == "IN":
        parking.add(car_licence)
    elif command == "OUT":
        parking.remove(car_licence)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
