# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on)
# and every even - quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].
# Input
# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop
# Output
# Gold -> 155
# Silver -> 10
# Copper -> 17
# Input
# gold
# 155
# silver
# 10
# copper
# 17
# gold
# 15
# stop
# Output
# gold -> 170
# silver -> 10
# copper -> 17
stock = {}

while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    if command not in stock.keys():
        stock[command] = quantity
    else:
        stock[command] += quantity

for (resource, quantity) in stock.items():
    print(f"{resource} -> {quantity}")
