# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
# Examples
# Input
# text
# Output
# t -> 2
# e -> 1
# x -> 1
# Input
# text text text
# Output
# t -> 6
# e -> 3
# x -> 3
words = input().split(" ")
some_dict = {}
for word in words:
    for ch in word:
        if ch not in some_dict.keys():
            some_dict[ch] = 1
        else:
            some_dict[ch] += 1
for (ch, count) in some_dict.items():
    print(f"{ch} -> {count}")