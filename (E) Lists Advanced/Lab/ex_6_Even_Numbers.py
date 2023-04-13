# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.
# Input	            Output
# 3, 2, 1, 5, 8	    [1, 4]

numbers = list(map(int, input().split(', ')))
indexes = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(indexes)
