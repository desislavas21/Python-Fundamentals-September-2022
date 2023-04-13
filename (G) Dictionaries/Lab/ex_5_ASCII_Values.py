# Write a program that receives a list of characters separated by ", ".
# It should create a dictionary with each character as a key and its ASCII value as a value.
# Try solving that problem using comprehension.
# Examples
# Input	            Output
# a, b, c, a	{'a': 97, 'b': 98, 'c': 99}
# d, c, m, h	{'d': 100, 'c': 99, 'm': 109, 'h': 104}
characters = input().split(", ")
result = {character: ord(character) for character in characters}
print(result)