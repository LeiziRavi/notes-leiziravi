grade = input("Enter grades: ")

grade_points = 0
counter = 0
while grade != "":
    if grade == "A+":
        grade_points += 4.0
    elif grade == "A":
        grade_points += 4.0
    elif grade == "A-":
        grade_points += 3.7
    elif grade == "B+":
        grade_points += 3.3
    elif grade == "B":
        grade_points += 3.0
    elif grade == "B-":
        grade_points += 2.7
    elif grade == "C+":
        grade_points += 2.3
    elif grade == "C":
        grade_points += 2.0
    elif grade == "C-":
        grade_points += 1.7
    elif grade == "D+":
        grade_points += 1.3
    elif grade == "D":
        grade_points += 1.0
    elif grade == "F":
        grade_points += 0

    counter += 1
    grade = input("Enter grades(blank to compute): ")

print("Average grade point: ", grade_points/counter)
