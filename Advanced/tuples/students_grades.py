n = int(input())
students = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for data in students.items():
    name, grades = data
    print(f"{name} -> {' '.join([f'{n:.2f}' for n in grades])} (avg: {(sum(grades)/len(grades)):.2f})")
