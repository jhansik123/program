def highest_average(students):
    highest_avg = 0
    top_student = None

    for student in students:
        avg = sum(student["grades"]) / len(student["grades"])
        if avg > highest_avg:
            highest_avg = avg
            top_student = student

    return top_student



students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [76, 82, 80]}
]

result = highest_average(students)
print(result)
