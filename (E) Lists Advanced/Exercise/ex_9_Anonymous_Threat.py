# Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative
# and unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you
# have been tasked to analyze the software of the virus and observe its actions on the data.
# You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII
# character except whitespace. Then you will begin receiving commands in one of the following formats:
# •	merge {startIndex} {endIndex}
# •	divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other
# words, you should concatenate them.
# Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index into several small
# substrings with equal length. The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last
# with equal lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements,
# joined by a space.
# Input	                        Output
# Ivo Johny Tony Bony Mony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1	                        IvoJohnyTonyBonyMony

# abcd efgh ijkl mnop qrst uvwx yz
# merge 4 10
# divide 4 5
# 3:1	                        abcd efgh ijkl mnop qr st uv wx yz
text = input().split(" ")


def merge(start_index, end_index):
    should_be_removed = []
    if start_index in range(0, len(text)) and end_index in range(0, len(text)):
        for index in range(start_index + 1, end_index+1):
            text[start_index] += text[index]
            should_be_removed.append(text[index])
    else:
        for index in range(start_index + 1, len(text)):
            text[start_index] += text[index]
            should_be_removed.append(text[index])
    for item in should_be_removed:
        text.remove(item)
    return text


def divide(index, partitions):
    word = text.pop(index)
    word_1 = []
    step = int(len(word) / partitions)
    if len(word) % partitions == 0:
        for i in range(0, len(word), 2):
            word_1.append(word[i:step+i])
    else:
        for i in range(0, len(word) - 1):
            if i == len(word) - 2:
                word_1.append(word[i:])
            else:
                word_1.append(word[i:step + i])
    for index_1 in range(len(word_1)-1, -1, -1):
        text.insert(index, word_1[index_1])
    return text


while True:
    command_1 = input()
    if command_1 == "3:1":
        break
    command = command_1.split(" ")
    action = command[0]
    start_index = int(command[1])
    end_index = int(command[-1])
    if action == "merge":
        merge(start_index, end_index)
    elif action == 'divide':
        divide(start_index, end_index)

print(" ".join(text))