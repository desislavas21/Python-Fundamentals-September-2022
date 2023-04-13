# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.
# Input
# 8, 12, 38, 3, 17, 19, 25, 35, 50
# Output
# Group of 10's: [8, 3]
# Group of 20's: [12, 17, 19]
# Group of 30's: [25]
# Group of 40's: [38, 35]
# Group of 50's: [50]
# Input
# 1, 3, 3, 4, 34, 35, 25, 21, 33
# Output
# Group of 10's: [1, 3, 3, 4]
# Group of 20's: []
# Group of 30's: [25, 21]
# Group of 40's: [34, 35, 33]

numbers = list(map(int, input().split(', ')))

for group in range(1, 11):
    if len(numbers) == 0:
        break
    group_l = [num for num in numbers if num <= group * 10]
    numbers = [num for num in numbers if num not in group_l]
    print(f"Group of {group}0's: {group_l}")

