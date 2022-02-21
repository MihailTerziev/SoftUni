from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
total_pizzas = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    current_employee = employees.pop()

    if current_order <= 0 or current_order > 10:
        employees.append(current_employee)
        continue

    if current_order > current_employee:
        current_order -= current_employee
        pizza_orders.appendleft(current_order)
        total_pizzas += current_employee
        continue

    total_pizzas += current_order

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(p) for p in pizza_orders])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(e) for e in employees])}")
