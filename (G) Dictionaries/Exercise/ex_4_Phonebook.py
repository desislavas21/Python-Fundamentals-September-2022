# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format:
# "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."
# Input
# Adam-0888080808
# 2
# Mery
# Adam
# Output
# Contact Mery does not exist.
# Adam -> 0888080808
# Input
# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# 4
# Silvester
# silvester
# Rolf
# Ralf
# Output
# Silvester -> 02/987665544
# Contact silvester does not exist.
# Contact Rolf does not exist.
# Ralf -> 666
phonebook = {}
while True:
    info = input().split("-")
    if len(info) > 1:
            phonebook[info[0]] = info[1]
    else:
        n = int(info[0])
        for _ in range(n):
            searched = input()
            if phonebook.get(searched):
                print(f"{searched} -> {phonebook[searched]}")
            else:
                print(f"Contact {searched} does not exist.")
        break

