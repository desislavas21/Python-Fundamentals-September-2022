# You will be receiving to-do notes until you get the command "End". The notes will be in
# the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Input
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End
# Output
# ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']

notes = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    com = command.split("-")
    priority = int(com[0]) - 1
    note = com[1]

    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)
