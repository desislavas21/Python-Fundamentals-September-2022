# You are given a secret message you should decipher.
# To do that, you need to know that in each word:
# the second and the last letter are switched (e.g., Holle means Hello)
# the first letter is replaced by its character code (e.g., 72 means H
# 72olle 103doo 100ya - Hello good day
# Input	                Output
# 72olle 103doo 100ya	Hello good day
# 82yade 115te 103o     Ready set go
code = input().split(" ")
final_code = []
for index in range(0, len(code)):
    if index == 0:
        word = code[0]
        number = int(word[0:2])
        fist_letter = chr(number)
        new_word = fist_letter + word[-1] + word[3:-1] + word[2]
        final_code.append(new_word)
    else:
        word = code[index]
        number = int(word[0:3])
        fist_letter = chr(number)
        new_word = fist_letter + word[-1] + word[4:-1] + word[3]
        final_code.append(new_word)


print(" ".join(final_code))