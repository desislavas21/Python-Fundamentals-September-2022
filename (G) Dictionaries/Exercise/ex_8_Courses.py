# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.
# Input
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end
# Output
# Programming Fundamentals: 2
# -- John Smith
# -- Linda Johnson
# JS Core: 1
# -- Will Wilson
# Java Advanced: 1
# -- Harrison White
# Input
# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end
# Output
# Algorithms: 2
# -- Jay Moore
# -- Bob Jackson
# Programming Basics: 1
# -- Martin Taylor
# Python Fundamentals: 3
# -- John Anderson
# -- Andrew Robinson
# -- Clark Lewis

d_course = {}
while True:
    command_1 = input()
    if command_1 == "end":
        break
    command = command_1.split(" : ")
    course_name = command[0]
    student = command[-1]
    if course_name not in d_course.keys():
        d_course[course_name] = [student]
    else:
        d_course[course_name].append(student)

for course, students in d_course.items():
    total = len(d_course[course])
    print(f"{course}: {total}")
    for student in students:
        print(f"-- {student}")
