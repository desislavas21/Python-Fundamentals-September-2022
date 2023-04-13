# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# •	"register {username} {license_plate_number}":
# o	The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
# o	If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# •	"unregister {username}":
# o	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# o	If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license plates in the format:
# •	"{username} => {license_plate_number}"
# Input
# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
# Output
# John registered CS1234JS successfully
# George registered JAVA123S successfully
# Andy registered AB4142CD successfully
# Jesica registered VR1223EE successfully
# Andy unregistered successfully
# John => CS1234JS
# George => JAVA123S
# Jesica => VR1223EE
# Input
# 4
# register Jony AA4132BB
# register Jony AA4132BB
# register Linda AA9999BB
# unregister Jony
# Output
# Jony registered AA4132BB successfully
# ERROR: already registered with plate number AA4132BB
# Linda registered AA9999BB successfully
# Jony unregistered successfully
# Linda => AA9999BB
# Input
# 6
# register Jacob MM1111XX
# register Anthony AB1111XX
# unregister Jacob
# register Joshua DD1111XX
# unregister Lily
# register Samantha AA9999BB
# Output
# Jacob registered MM1111XX successfully
# Anthony registered AB1111XX successfully
# Jacob unregistered successfully
# Joshua registered DD1111XX successfully
# ERROR: user Lily not found
# Samantha registered AA9999BB successfully
# Anthony => AB1111XX
# Joshua => DD1111XX
# Samantha => AA9999BB

d_parking = {}
n = int(input())

for _ in range(n):
    info = input().split(" ")
    if info[0] == "register":
        username = info[1]
        license_number = info[-1]

        if username in d_parking.keys():
            existing_plate = d_parking[username]
            print(f"ERROR: already registered with plate number {existing_plate}")
        else:
            d_parking[username] = license_number
            print(f"{username} registered {license_number} successfully")

    elif info[0] == "unregister":
        action = info[0]
        username = info[-1]

        if username not in d_parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del d_parking[username]

for username, license_number in d_parking.items():
    print(f"{username} => {license_number}")

