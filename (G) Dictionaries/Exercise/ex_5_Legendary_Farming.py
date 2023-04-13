# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
# Input
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards
# Output
# Valanyr obtained!
# shards: 5
# fragments: 5
# motes: 3
# stones: 5
# leathers: 6
# Input
# 123 silver 6 shards 8 shards 5 motes
# 9 fangs 75 motes 103 MOTES 8 Shards
# 86 Motes 7 stones 19 silver
# Ouput
# Dragonwrath obtained!
# shards: 22
# fragments: 0
# motes: 19
# silver: 123
# fangs: 9

d_note = {}
while True:
    command = (input().lower()).split(" ")
    for index in range(1, len(command), 2):
        if command[index] not in d_note.keys():
            d_note[command[index]] = int(command[index-1])
            if d_note["shards"] >= 250 or d_note["fragments"] >= 250 or d_note["motes"] >= 250:
                break
        else:
            d_note[command[index]] += int(command[index - 1])
            if d_note["shards"] >= 250 or d_note["fragments"] >= 250 or d_note["motes"] >= 250:
                break