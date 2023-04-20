grade = input("Enter grade: ")

grade_points = 0
if grade == "A+":
    grade_points = 4.0
elif grade == "A":
    grade_points = 4.0
elif grade == "A-":
    grade_points = 3.7
elif grade == "B+":
    grade_points = 3.3
elif grade == "B":
    grade_points = 3.0
elif grade == "B-":
    grade_points = 2.7
elif grade == "C+":
    grade_points = 2.3
elif grade == "C":
    grade_points = 2.0
elif grade == "C-":
    grade_points = 1.7
elif grade == "D+":
    grade_points = 1.3
elif grade == "D":
    grade_points = 1.0
elif grade == "F":
    grade_points = 0
else:
    grade_points = "Invalid Grades."

print(f"{grade} is equal to {grade_points} Grade Points.")
