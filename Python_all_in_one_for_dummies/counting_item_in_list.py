# Create a list of strings
grades = ["C","B","A","D","C","B","C"]

# Count the B's
b_grades = grades.count("B")

# Use a variable for the value to count.
look_for= "C"
c_grades = grades.count(look_for)

print("There are " + str(b_grades) + " B grades in the list.")
print("There are " + str(c_grades) + " " + look_for + " grades in the list.")
203..
# Count Fs too.
print("There are " + str(grades.count("F")) + " F grades in the list.")