# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
# Input
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5
# Output
# John -> 5.00
# Alice -> 4.50
# George -> 5.00
# Input
# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6
# Output
# Rob -> 5.50
# Christian -> 5.00
# Robert -> 6.00

n = int(input())
d_marks = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in d_marks:
        d_marks[name] = [grade]
    else:
        d_marks[name].append(grade)

for student, grade in d_marks.items():
    average = sum(d_marks[student])/len(d_marks[student])
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")
