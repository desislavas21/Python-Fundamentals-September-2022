# Using comprehension, write a program that receives some text, separated by space,
# and take only those words whose length is even. Print each word on a new line.
# Example
# Input	                        Output
# kiwi orange banana apple	    kiwi
#                               orange
#                               banana
# pizza cake pasta chips	    cake

words = input().split(" ")
even_words = [word for word in words if len(word) % 2 == 0]
for word in even_words:
    print(word)
