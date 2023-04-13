# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"
# Input	            Output
# 1 2 3 4 2 1
# 3	                Score: 2/6. Employees are not happy!
# Input	            Output
# 2 3 2 1 3 3
# 4	                Score: 3/6. Employees are happy!
happiness = list(map(int, input().split(' ')))
people = len(happiness)
factor = int(input())
happiness = list(map(lambda number: number * factor, happiness))
average = sum(happiness) / len(happiness)
happier = list(filter(lambda number: number >= average, happiness))

if len(happier) >= (people/2):
    print(f"Score: {len(happier)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happier)}/{len(happiness)}. Employees are not happy!")