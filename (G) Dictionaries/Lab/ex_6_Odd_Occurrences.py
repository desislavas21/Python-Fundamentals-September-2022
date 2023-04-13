# Write a program that prints all elements from a given sequence of words that occur an odd number of times
# (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.
# Input	                                Output
# Java C# PHP PHP JAVA C java	        java c# c
# 3 5 5 hi pi HO Hi 5 ho 3 hi pi	    5 hi
# a a A SQL xx a xx a A a XX c	        a sql xx c

words = input().split(" ")
words = [word.lower() for word in words]
items = {}

for word in words:
    if word not in items:
        items[word] = 1
    else:
        items[word] += 1

for (item,  occurences ) in items.items():
    if occurences % 2 != 0:
        print(item, end=" ")