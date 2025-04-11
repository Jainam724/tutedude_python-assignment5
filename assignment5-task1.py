stud_marks = {
    'Ramesh': 85,
    'Jainam': 92,
    'Dev': 78,
    'Aditya': 90,
    'Daksh': 88
}

name = input("Enter the name of the student: ")
if name in stud_marks:
    print(f"{name}'s marks are {stud_marks[name]}")
else:
    print(f"{name} named Student not found")