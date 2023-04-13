# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
# Output
# SoftUni
# -- AA12345
# -- BB12345
# Microsoft
# -- CC12345
# HP
# -- BB12345
# Input
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End
# Output
# SoftUni
# -- AA12345
# -- CC12344
# Lenovo
# -- XX23456
# Movement
# -- DD11111

database = {}
while True:
    command_1 = input()
    if command_1 == "End":
        break
    command = command_1.split(" -> ")
    company = command[0]
    employee = command[-1]
    if company not in database.keys():
        database[company] = [employee]
    else:
        if employee not in database[company]:
            database[company].append(employee)

for company in database.keys():
    print(company)
    for employee in database[company]:
        print(f"-- {employee}")
