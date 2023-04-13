# Everybody knows that you spend too much time awake during nighttime.
# Your task is to define how much coffee you need to stay awake. Until you receive the command "END",
# you need to read commands on different lines.
# According to the commands, calculate the number of coffees you need to drink to stay awake during the daytime.
# The list of events can contain the following:
# · You have homework to do ("coding").
# · You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# · You watch a movie ("movie").
# · If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
# · If it is lowercase, you need 1 coffee by an event.
# · If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".
# Example
# Input
# dog
# CAT
# gaming
# END
# Output
# 3

# Input
# movie
# CODING
# MOVIE
# CLEANING
# cat
# END
# Output
# You need extra sleep

command = input()
coffee = 0

while True:
    if command != 'END':
        if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
            coffee += 1
        elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
            coffee += 2
    else:
        break
    command = input()

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")