# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"
# Example
# Input	    Output
# 5         [10, 3, 2]
# 10        [-15, -4]
# 3         Count of positives: 3
# 2         Sum of negatives: -19
# -15
# -4
# Input	    Output
# 6         [11, 2, 35, 599, 31, 20]
# 11        []
# 2         Count of positives: 6
# 35        Sum of negatives: 0
# 599
# 31
# 20

n = int(input())
positive = []
negative = []
for i in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
count_p = len(positive)
sum_n = sum(negative)
print(positive)
print(negative)
print(f"Count of positives: {count_p}")
print(f"Sum of negatives: {sum_n}")