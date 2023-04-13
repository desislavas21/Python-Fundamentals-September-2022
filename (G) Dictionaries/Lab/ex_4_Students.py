# You will be receiving names of students, their ID,
# and a course of programming they have taken in the format "{name}:{ID}:{course}". On the last line, you will receive
# a name of a course in snake case lowercase letters. You should print only the information of the students who have taken
# the corresponding course in the format: "{name} - {ID}" on separate lines.
# Input
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals
# Output
# John - 5622
# Maya - 89
# Lilly - 633
# Input
# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics
# Output
# Alex - 6
# Maria - 7

# 1
data = {}
course = ''
while True:
    command = input()
    try:
        name, id, course = command.split(':')
        data[name] = [id, course]
    except ValueError:
        course = command.replace("_", " ")
        break

for name, [id, current_course] in data.items():
    if current_course == course:
        print(f"{name} - {id}")

# 2
students = {}
command = input().split(":")

while len(command) > 1:
    name, id, course = command[0], command[1], command[2]
    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {id}")
    command = input().split(":")
searched_course = command[0].replace("_", " ")
for student in students[searched_course]:
    print(student)