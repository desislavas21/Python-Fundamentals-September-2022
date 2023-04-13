# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line, which are substrings
# of any string in the second input line.
# Input	                                    Output
# arp, live, strong
# lively, alive, harp, sharp, armstrong	    ['arp', 'live', 'strong']
# Input	Output
# tarp, mice, bull
# lively, alive, harp, sharp, armstrong     []

# 1
first = input().split(", ")
second = input().split(", ")
result = list(set([word for word in first for word_1 in second if word in word_1]))
print(result)

# 2
first = input().split(", ")
second = input().split(", ")
which = []
for word in first:
    for whole in second:
        if word in whole:
            which.append(word)
            break
print(which)